# Public libraries
from PySide6 import QtCore
from PySide6.QtSerialPort import QSerialPortInfo, QSerialPort
from PySide6.QtCore import QTimer 

# Private libraries
from shared.mainwindow import MainWindow
from shared.telegram_manager import TelegramManager
from shared.encoder_data import EncoderData

class SerialBox:
    def __init__(self, main_window: MainWindow, 
                 manager: TelegramManager,
                 encoder: EncoderData):

        # Setup shared classes
        self.main_window = main_window
        self.manager = manager
        self.encoder = encoder
        
        # Search for all main components in the MainWindow  
        self.conn_button = self.main_window.ui.com_connect_button
        self.disc_button = self.main_window.ui.com_disconnect_button
        self.com_select_list = self.main_window.ui.com_available_combo
        self.ppr1_spinbox = self.main_window.ui.ppr1_spinbox
        self.ppr2_spinbox = self.main_window.ui.ppr2_spinbox
        self.diameter_spinbox = self.main_window.ui.diameter_spinbox
        self.com_update_timer = QTimer()
        self.quit_timer = QTimer()
        
        # Inizialization
        self.quit_timer.setSingleShot(True)
        self.com_update_timer.start(100)
        self.manager.setBaudRate(115200)
        self.main_window.set_permanent_message(f"Not connected 🔴")
        
        # Internal slots
        self.com_update_timer.timeout.connect(self.update_available_COMs)
        self.conn_button.clicked.connect(self.connect_to_COM)
        self.disc_button.clicked.connect(self.disconnect_to_COM)
        self.manager.errorOccurred.connect(self.cable_disconnection_action)
        self.manager.unknown_board_detected.connect(self.unknown_board_action)
        self.main_window.about_to_quit.connect(self.closing_gui_procedure)
        
        # External slots
        self.manager.aboutToClose.connect(
            self.main_window.serial_box_interface_to_disconnected)
        self.quit_timer.timeout.connect(self.main_window.close_app)
    
    def closing_gui_procedure(self):
        if self.manager.isOpen():
            self.manager.assign_disconnection_telegram()
            self.quit_timer.start(500)
        
        self.main_window.close()
        
    def update_available_COMs(self):  
        
        # Get all the current available COM ports
        available_ports = []
        for info in QSerialPortInfo.availablePorts():
            if info.portName() != self.manager.portName():
                available_ports.append(info.portName())
        
        # If the previous COM list is not equal to the current, then
        # I redraw the available COMs in the combo box
        # * its done to prevent the combo box flickering bug
        if len(available_ports) != self.com_select_list.count():
            # Fill the combo box with all the port names
            self.com_select_list.clear()
            self.com_select_list.insertItems(0, available_ports)
        
    def connect_to_COM(self):
        # ! Test - check if I'm already connected, the program should
        # ! never go here
        if self.manager.portName() != "":
            msg = "The app tried to connect to multiple serial devices"
            raise Exception(msg)
        
        # Check if there are no ports to connect to
        if self.com_select_list.currentText() == "":
            self.show_no_ports_available_message()
            return
        
        for info in QSerialPortInfo.availablePorts():
            if info.portName() == self.com_select_list.currentText():
                self.manager.setPort(info)
                if self.manager.open(QSerialPort.ReadWrite):
                    self.show_connection_success_message()
                    
                    self.main_window.serial_box_interface_to_connected()
                    self.main_window.single_value_to_enabled()
                    self.main_window.curve_emulation_to_enabled()
                    self.update_encoder_object_costants()
                    self.send_costants_via_serial()
                    self.encoder.reset_variables()
                else:
                    self.show_connection_failed_message()
                    self.manager.close_serial_connection()
                break
                
    def disconnect_to_COM(self):
        # ! Test - check if I'm already disconnected, the program should
        # ! never go here
        if self.manager.portName() == "":
            msg_pt1 = "The app tried to disconnect from serial device"
            msg_pt2 = "while it was already disconnected"
            msg = f"{msg_pt1} {msg_pt2}"
            raise Exception(msg)
        
        self.show_disconnection_message()
        self.manager.assign_disconnection_telegram()
            
    def cable_disconnection_action(self):
        # Test - check if the error is due to a cable disconnection
        if self.manager.error() == QSerialPort.ResourceError:
            self.show_cable_disconnection_message()
            self.manager.close_serial_connection()
    
    def unknown_board_action(self):
            self.manager.close_serial_connection()
            self.show_unknown_board_message()
        
    def send_costants_via_serial(self):
        # Fetch the user values from the spinboxes
        diameter = self.encoder.diameter
        ppr1 = self.encoder.ppr_e1
        ppr2 = self.encoder.ppr_e2 
        
        # Call the manager in order to send a connection telegram
        self.manager.send_connection_telegram(diameter, ppr1, ppr2)
       
    def update_encoder_object_costants(self):
        self.encoder.diameter = self.diameter_spinbox.value()
        self.encoder.ppr_e1 = self.ppr1_spinbox.value()
        self.encoder.ppr_e2 = self.ppr2_spinbox.value()
      
    # ******************************************************************
    # * MESSAGES DEFINITIONS
    # ******************************************************************
        
    def show_connection_success_message(self):
        # Connection success - permanent message
        message = f"Connected to {self.manager.portName()} 🟢"
        self.main_window.set_permanent_message(message)
        
        # Connection success - temporary message
        message = "Connected successfully!"
        self.main_window.set_temporary_message(message)
       
    def show_connection_failed_message(self):
        # Failure to connect - temporary message
        message = f"Unable to connect to {self.manager.portName()}"
        self.main_window.set_temporary_message(message)
        
    def show_disconnection_message(self):
        # Disconnection - permanent message
        message = "Not connected 🔴"
        self.main_window.set_permanent_message(message)
        
        # Disconnection - temporary message
        message = "Disconnected successfully!"
        self.main_window.set_temporary_message(message)
    
    def show_no_ports_available_message(self):
        # Temporary message
        message = "No ports to connect to!"
        self.main_window.set_temporary_message(message)
        
    def show_cable_disconnection_message(self):
            # Cable disconnection - temporary message
            message = " Cable disconnected!"
            self.main_window.set_temporary_message(message)
            
            # Cable disconnection - permanent message
            message = "Not connected 🔴"
            self.main_window.set_permanent_message(message)
            
    def show_unknown_board_message(self):
            # Cable disconnection - temporary message
            message = " The device is not a GITSIM board!"
            self.main_window.set_temporary_message(message)
            
            # Cable disconnection - permanent message
            message = "Not connected 🔴"
            self.main_window.set_permanent_message(message)