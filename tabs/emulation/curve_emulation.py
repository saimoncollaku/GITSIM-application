# Public libraries
from PySide6.QtWidgets import QFileDialog
from pyqtgraph import PlotWidget
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
        self.choose_file_button = self.main_window.ui.pushButton_4
        self.plot_widget = self.main_window.ui.plot_widget
        self.speed_axis_radio = self.main_window.ui.radioButton
        self.acc_axis_radio = self.main_window.ui.radioButton_2
        
        # Variables for file reading 
        self.data_frame = None
        self.curve_data = None
        self.setup_plot_widget()
        
        # Setup signal connections
        self.choose_file_button.clicked.connect(self.load_emulation_file)
        self.acc_axis_radio.pressed.connect(self.set_acc_axis)
        self.speed_axis_radio.pressed.connect(self.set_speed_axis)   
        
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
                self.data = self.data_frame.astype(float).to_numpy()
                self.plot_data_collected()
                
                file_name = os.path.basename(file_path)
                # Do something with the data
                print(f"Loaded file: {file_name}")
                print(f"Number of rows: {self.data.shape[0]}")
                print(f"First row: {self.data[0] if self.data.size else 'Empty file'}")
                return
            
            except Exception:
                print(f"Error reading file")
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
        self.plot_widget.setLabel('left', 'Speed [m/s]')
        self.plot_widget.setLabel('bottom', 'Time [s]')
        
    def plot_data_collected(self):
        x = np.arange(0, len(self.data) * 0.05, 0.05)
        curve1 = self.plot_widget.plot(x, self.data[:, 0], pen='b', name='Curve 1')
        curve2 = self.plot_widget.plot(x, self.data[:, 1], pen='r', name='Curve 2')
        self.plot_widget.addLegend(["Encoder 1", "Encoder 2"])
        self.plot_widget.setYRange(min(self.data.min(), 0), max(self.data.max(), 0))   
        self.plot_widget.setXRange(0, x[-1]) 
        
    def set_acc_axis(self):
        self.plot_widget.setLabel('left', 'Acceleration [m/s²]')   
        
    def set_speed_axis(self):
        self.plot_widget.setLabel('left', 'Speed [m/s]')  