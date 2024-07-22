# Public libraries
from PySide6.QtWidgets import QFileDialog
from pyqtgraph import LegendItem, InfiniteLine
from PySide6.QtCore import QTimer

import pandas as pd
import os
import numpy as np

# Private libraries
from shared.mainwindow import MainWindow
from shared.telegram_manager import TelegramManager
from shared.encoder_data import EncoderData


class CurveEmulation():
    def __init__(self, main_window: MainWindow, 
                    manager: TelegramManager,
                    encoder: EncoderData):
        
        # Setup shared resources
        self.main_window = main_window
        self.manager = manager
        self.encoder = encoder
        
        # Setup exclusive resources
        self.choose_file_button = self.main_window.ui.choose_emu_file_button
        self.plot_widget = self.main_window.ui.plot_widget
        self.speed_axis_radio = self.main_window.ui.speed_emulation_radio
        self.acc_axis_radio = self.main_window.ui.acc_emulation_radio
        self.start_curve_button = self.main_window.ui.start_emulation_button
        self.stop_curve_button = self.main_window.ui.stop_emulation_button
        self.initial_speed_spinbox = self.main_window.ui.init_speed_spinbox
        self.choose_folder_button = self.main_window.ui.log_folder_button
        self.log_name_edit = self.main_window.ui.log_name_edit
        
        
        # Variables for file reading 
        self.data_frame = None
        self.curve_data = None
        self.curve1 = None
        self.curve2 = None
        self.current_index = 0
        self.log_folder_path = os.path.dirname(os.path.abspath(__file__))
        self.log_data = np.empty((0,5))
        self.log_name = "Log_test.xlsx"
        
        # Timer for moving vertical line
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_vertical_line)
        self.setup_plot_widget()
        
        # Setup signal connections
        self.choose_file_button.clicked.connect(self.load_emulation_file)
        self.acc_axis_radio.pressed.connect(self.set_acc_axis)
        self.speed_axis_radio.pressed.connect(self.set_speed_axis)
        self.choose_folder_button.pressed.connect(self.select_log_folder)
        self.manager.aboutToClose.connect(self.disconnection_action)
        self.start_curve_button.pressed.connect(self.start_curve_emulation)
        self.stop_curve_button.pressed.connect(self.stop_curve_emulation)
        
    def load_emulation_file(self):
        
        file_path = self.open_choose_file_dialog()
        
        if file_path != None:
                
            # Try to get access to the file
            file_extension = os.path.splitext(file_path)[1].lower()
            
            try:
                if not self.check_file_extension(file_path, file_extension):
                    print(f"Unsupported file type")
                    return
                
                if not self.check_number_of_columns():
                    print(f"File should have exactly 2 columns.")
                    return
                
                if not self.check_values_are_numeric():
                    print("All values in the file should be numeric.")
                    return
                
                # Convert to numpy array of float64
                self.curve_data = self.data_frame.astype(float).to_numpy()
                self.plot_data_collected()
                print("111")
                file_name = os.path.basename(file_path)
                
                # Do something with the data
                print(f"Loaded file: {file_name}")
                print(f"Number of rows: {self.curve_data.shape[0]}")
                print(f"First row: {self.curve_data[0] if self.curve_data.size else 'Empty file'}")
                print(self.curve_data)
                
                self.main_window.curve_emulation_to_can_emulate()
                return
            
            except Exception:
                print(f"Error reading file")
                self.main_window.curve_emulation_to_enabled()
                return            

    def check_values_are_numeric(self) -> bool:
        # Attempt to convert all columns to numeric
        numeric_df = self.data_frame.apply(pd.to_numeric, errors='coerce')
        
        # Check if any null values were introduced 
        return not numeric_df.isnull().any().any()
    
    def check_file_extension(self, path: str, extension: str) -> bool:
        if extension in ['.xlsx', '.xls']:
            self.data_frame = pd.read_excel(path, header=None)
            return True
        elif extension == '.csv':
            self.data_frame = pd.read_csv(path, header=None)
            return True
        return False
                    
    def check_number_of_columns(self) -> bool:
        if self.data_frame.shape[1] == 2:
            return True
        else:
            return False
    
    def open_choose_file_dialog(self) -> str:
        """Opens the dialog window, where its possible to choose 
        csv/xlsx/xls file types

        Returns:
            str: the chosen file filepath, returns 'None' if nothing is chosen
        """
        window_name = "Choose emulation file"
        file_types = ["Excel Files (*.xlsx *.xls)",
                    'CSV Files (*.csv)']
        permitted_file_types = ";;".join(file_types)
        
        # Open file dialog
        file_dialog = QFileDialog(None, window_name, "", permitted_file_types)
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        
        if file_dialog.exec() == QFileDialog.DialogCode.Accepted:
            # Pick only the first selected file
            file_path = file_dialog.selectedFiles()[0]
            return file_path
        else:
            return None
 
    def setup_plot_widget(self):
        self.plot_widget.setMouseEnabled(x=False, y=False)
        self.plot_widget.setMenuEnabled(False)
        self.plot_widget.hideButtons()
        self.plot_widget.setLimits(xMin=None, xMax=None, yMin=None, yMax=None)
        self.plot_widget.showGrid(x=True, y=True, alpha=0.3)
        self.plot_widget.setBackground("w")
        self.plot_widget.getViewBox().setBackgroundColor(None)
        self.plot_widget.getPlotItem().getViewBox().setBorder(pen=None)
        self.plot_widget.setLabel('left', 'Speed [m/s]', color='k', size='12pt')
        self.plot_widget.setLabel('bottom', 'Time [s]', color='k', size='12pt')
        
        # Change the color of the labels to black
        self.plot_widget.getAxis('left').setPen('k')  # 'k' stands for black
        self.plot_widget.getAxis('left').setTextPen('k')
        self.plot_widget.getAxis('bottom').setPen('k')
        self.plot_widget.getAxis('bottom').setTextPen('k')

        # Create the legend item and set its offset to be below the x-axis
        self.legend = LegendItem((80, 60), offset=(-10, 10))
        self.legend.setParentItem(self.plot_widget.getPlotItem())
        
        self.curve1 = self.plot_widget.plot([], [], pen={'color': 'b', 'width': 3}, name="Encoder 1")
        self.curve2 = self.plot_widget.plot([], [], pen={'color': 'r', 'width': 3}, name="Encoder 2")
        self.legend.addItem(self.curve1, '<span style="color: black;">Encoder 1</span>')
        self.legend.addItem(self.curve2, '<span style="color: black;">Encoder 2</span>')
        
        self.legend.setBrush((200, 200, 200, 150))  # Grey background with some transparency
        self.legend.setLabelTextColor('k')
        
        # Add a vertical line
        self.vertical_line = InfiniteLine(angle=90, movable=False, pen='g')
        self.plot_widget.addItem(self.vertical_line)
        self.vertical_line_position = 0
        
    def plot_data_collected(self):
        # Calculate x-axis range
        x = np.arange(0, len(self.curve_data) * 0.05, 0.05)
        
        # Remove existing curves
        self.plot_widget.removeItem(self.curve1)
        self.plot_widget.removeItem(self.curve2)
        
        # Setting the curves specs
        pen1 = {'color': 'b', 'width': 3}
        pen2 = {'color': 'r', 'width': 3}
        self.curve1 = self.plot_widget.plot(x, self.curve_data[:, 0], 
                                       pen=pen1, name="Encoder 1")
        self.curve2 = self.plot_widget.plot(x, self.curve_data[:, 1], 
                                       pen=pen2, name="Encoder 1")
        max_y = max(self.curve_data.max(), 0)
        min_y = min(self.curve_data.min(), 0)
        self.plot_widget.setYRange(max_y, min_y)   
        self.plot_widget.setXRange(0, x[-1], padding=0) 
        
        # Reset and start the vertical line movement
        self.vertical_line_position = 0
        self.vertical_line.setPos(self.vertical_line_position)
        self.timer.start(100)  # update every 100ms
        
    def update_vertical_line(self):
        self.vertical_line_position += 0.05
        
        if self.vertical_line_position >= (len(self.curve_data) - 1) * 0.05:
            self.timer.stop()
            return
        
        self.vertical_line.setPos(self.vertical_line_position)
        print(self.vertical_line_position)    
        
    def set_acc_axis(self):
        self.plot_widget.setLabel('left', 'Acceleration [m/s²]', color='k', size='12pt') 
        self.initial_speed_spinbox.setEnabled(True) 
        
    def set_speed_axis(self):
        self.plot_widget.setLabel('left', 'Speed [m/s]', color='k', size='12pt')
        self.initial_speed_spinbox.setEnabled(False)
  
    def disconnection_action(self):
        self.main_window.curve_emulation_to_disabled()
        self.log_data = np.empty((0,5))
        self.plot_widget.removeItem(self.curve1)
        self.plot_widget.removeItem(self.curve2)
  
    def start_curve_emulation(self):
        # Change interface appearance
        self.main_window.curve_emulation_to_emulating()
        
        self.encoder.variables_updated.connect(self.curve_emulation_action)
        
    def stop_curve_emulation(self):
        self.start_curve_button.setChecked(False)
        self.main_window.curve_emulation_to_can_emulate()     
        
    def curve_emulation_action(self):
        
        if self.speed_axis_radio.isChecked():
            self.send_speed_curve_data()
        elif self.acc_axis_radio.isChecked():
            pass
        else:
            msg_pt1 = "The app tried to disconnect to emulate an"
            msg_pt2 = "unknown type of curve!"
            msg = f"{msg_pt1} {msg_pt2}"
            raise Exception(msg)
    
    # ******************************************************************
    # * APP/BOARD INTERACTION METHODS
    # ******************************************************************
        
    def send_speed_curve_data(self):
        if self.current_index == 0:
            self.send_first_speed_curve_data()
        elif self.current_index == self.curve_data.shape[0]:
            self.send_last_speed_curve_data()
        else:
            self.send_generic_speed_curve_data()
        
    def send_first_speed_curve_data(self):
        speed1 = self.curve_data[0, 0]
        speed2 = self.curve_data[0, 1]
        self.manager.assign_speed_both_telegram(speed1, speed2)
        self.current_index += 1
        
    def send_generic_speed_curve_data(self):
        delta_t = 0.05
        # Calculate acceleration for Encoder 1
        speed1 = self.curve_data[self.current_index, 0] 
        speed1_prec = self.curve_data[self.current_index - 1, 0] 
        acc1 = (speed1 - speed1_prec) / delta_t
        # Calculate acceleration for Encoder 1
        speed2 = self.curve_data[self.current_index, 1] 
        speed2_prec = self.curve_data[self.current_index - 1, 1] 
        acc2 = (speed2 - speed2_prec) / delta_t
        self.current_index += 1
        self.manager.assign_acc_both_telegram(acc1, acc2)
        
    def send_last_speed_curve_data(self):
        self.manager.assign_reset_kine_telegram()
        self.current_index = 0
        self.encoder.variables_updated.disconnect(self.curve_emulation_action)
        self.stop_curve_emulation()
        
    def send_acc_curve_data(self):
        if self.current_index == 0:
            self.send_first_acc_curve_data()
        elif self.current_index == self.curve_data.shape[0]:
            self.send_last_acc_curve_data()
        else:
            self.send_generic_acc_curve_data()
            
    def send_first_acc_curve_data(self):
        speed1 = self.initial_speed_spinbox.value
        speed2 = self.initial_speed_spinbox.value
        self.manager.assign_speed_both_telegram(speed1, speed2)
        
    def send_generic_acc_curve_data(self):
        acc1 = self.curve_data[self.current_index, 0] 
        acc2 = self.curve_data[self.current_index, 1] 
        self.manager.assign_acc_both_telegram(acc1, acc2)
        self.current_index += 1
    
    def send_last_acc_curve_data(self):
        
        acc1 = self.curve_data[self.current_index, 0] 
        acc2 = self.curve_data[self.current_index, 1] 
        self.manager.assign_acc_both_telegram(acc1, acc2)
    
    # ******************************************************************
    # * LOG DATA METHODS
    # ******************************************************************
    
    def select_log_folder(self):
        folder_path = QFileDialog.getExistingDirectory(None, "Select Folder")
        
        if folder_path:
            # Construct full file path
            file_name = "your_file.xls"
            
            df = pd.DataFrame(np.random.rand(10, 4), columns=['Speed', 'B', 'C', 'D'])

            file_name = "your_file.xlsx"
            full_path = os.path.join(folder_path, file_name)

            # Save the DataFrame as an XLSX file
            df.to_excel(full_path, index=False)

            print(f"File saved to: {full_path}")
        else:
            print("Folder selection canceled")
            
    def create_and_save_log_file(self):
        labels = ["Time", 'Speed_E1', 'Speed_E2', 'Count_E1', 'Count_E2']
        df = pd.DataFrame(self.data_log, columns=labels)
        
    def save_encoder_data(self):
        c1 = self.encoder.counter_e1
        c2 = self.encoder.counter_e2
        s1 = self.encoder.speed_e1
        s2 = self.encoder.speed_e2
        
        new_row = np.array([[0, c1, c2, s1, s2]])
        self.data_log = np.vstack((self.data_log, new_row))    
        