# Public libraries
from PySide6 import QtCore
from PySide6.QtSerialPort import QSerialPortInfo, QSerialPort
import struct

# Private libraries
from classes.mainwindow.mainwindow_class import MainWindow

class SerialBox:
    def __init__(self, main_window: MainWindow, serial_port: QSerialPort):

        # Setup shared classes
        self.main_window = main_window
        self.serial_port = serial_port
        
        # Search for all main components in the MainWindow  
        self.conn_button = self.main_window.ui.com_connect_button
        self.disc_button = self.main_window.ui.com_disconnect_button
        self.com_select_list = self.main_window.ui.com_available_combo
        self.ppr_encoder1_edit = self.main_window.ui.ppr_encoder1_edit
        self.ppr_encoder2_edit = self.main_window.ui.ppr_encoder2_edit
        self.wheel_diameter_edit = self.main_window.ui.wheel_diameter_edit
        self.com_update_timer = QtCore.QTimer()
        
        # Inizialization
        self.com_update_timer.start(100)
        self.serial_port.setBaudRate(115200)
        self.main_window.set_permanent_message(f"Not connected 🔴")
        
        # Assign slots to the signals
        self.com_update_timer.timeout.connect(self.update_available_COMs)
        self.conn_button.clicked.connect(self.connect_to_COM)
        self.disc_button.clicked.connect(self.disconnect_to_COM)
        self.serial_port.errorOccurred.connect(self.cable_disconnection_action)
        
    def update_available_COMs(self):  
        
        # Get all the current available COM ports
        available_ports = []
        for info in QSerialPortInfo.availablePorts():
            if info.portName() != self.serial_port.portName():
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
        # ! never go here, its for debug purposes!
        if self.serial_port.portName() != "":
            message = "DEBUG - Already connected!"
            self.main_window.set_temporary_message(message)
            return
        
        # Check if there are no ports to connect to
        if self.com_select_list.currentText() == "":
            message = "No ports to connect to!"
            self.main_window.set_temporary_message(message)
            return
        
        for info in QSerialPortInfo.availablePorts():
            if info.portName() == self.com_select_list.currentText():
                self.serial_port.setPort(info)
                if self.serial_port.open(QSerialPort.ReadWrite):
                    # Connection success - permanent message
                    message = f"Connected to {info.portName()} 🟢"
                    self.main_window.set_permanent_message(message)
                    
                    # Connection success - temporary message
                    message = "Connected successfully!"
                    self.main_window.set_temporary_message(message)
                    
                    # Change enable state of buttons
                    self.conn_button.setEnabled(False)
                    self.disc_button.setEnabled(True)
                    
                    self.send_connection_telegram()
                else:
                    # Failure to connect - temporary message
                    message = f"Unable to connect to {info.portName()}"
                    self.main_window.set_temporary_message(message)
                    
                    # Closing connection procedure
                    self.serial_port.close()
                    self.serial_port.setPortName("")
                break
                
    def disconnect_to_COM(self):
        # ! Test - check if I'm already disconnected, the program should
        # ! never go here, its for debug purposes
        if self.serial_port.portName() == "":
            message = "DEBUG - Already disconnected!"
            self.main_window.set_temporary_message(message)
            return
        
        # Disconnection - permanent message
        message = "Not connected 🔴"
        self.main_window.set_permanent_message(message)
        
        # Disconnection - temporary message
        message = "Disconnected successfully!"
        self.main_window.set_temporary_message(message)

        # Closing connection procedure
        self.serial_port.close()
        self.serial_port.setPortName("")
        
        # Change enable state of buttons
        self.conn_button.setEnabled(True)
        self.disc_button.setEnabled(False) 
            
    def cable_disconnection_action(self):
        # Test - check if the error is due to a disconnection
        if self.serial_port.error() == QSerialPort.ResourceError:
            # Cable disconnection - temporary message
            message = " Cable disconnected!"
            self.main_window.set_temporary_message(message)
            
            # Cable disconnection - permanent message
            message = "Not connected 🔴"
            self.main_window.set_permanent_message(message)
            
            # Closing connection procedure
            self.serial_port.close()
            self.serial_port.setPortName("") 
            
            # Change enable state of buttons
            self.conn_button.setEnabled(True)
            self.disc_button.setEnabled(False)
    
    def send_connection_telegram(self):
        # ppr_encoder1 = int(self.ppr_encoder1_edit.text())
        # ppr_encoder2 = int(self.ppr_encoder2_edit.text())  
        # wheel_diameter = float(self.wheel_diameter_edit.text())
        
        ppr_encoder1 = 89
        ppr_encoder2 = 98 
        wheel_diameter = 1.06
        
        telegram = struct.pack('<fHH',  wheel_diameter,
                                        ppr_encoder1, 
                                        ppr_encoder2)
        self.serial_port.write(telegram)
        print(telegram[0])
        
        