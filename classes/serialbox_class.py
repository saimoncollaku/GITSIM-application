# Public libraries
from PySide6 import QtWidgets, QtCore
from PySide6.QtSerialPort import QSerialPortInfo, QSerialPort
import struct

from classes.mainwindow_class import MainWindow

class SerialBox:
    def __init__(self, main_window: MainWindow, serial_port: QSerialPort):

        # Setup shared classes
        self.main_window = main_window
        self.serial_port = serial_port
        
        # Search for all main components in the MainWindow  
        self.conn_button = self.main_window.ui.com_connect_button
        self.disc_button = self.main_window.ui.com_disconnect_button
        self.com_select_list = self.main_window.ui.com_available_combo
        self.com_update_timer = QtCore.QTimer()
        
        # Inizialization
        self.com_update_timer.start(100)
        self.serial_port.setBaudRate(9600)
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
    
    # def read_data(self):
    #     while self.serial_port.canReadLine():
    #         data = self.serial_port.readLine().data().decode('utf-8').strip()
    #         print(f"Received: {data}")
    
    # def read_data(self):
    #     while self.serial_port.bytesAvailable() >= 17:  # Ensure we have enough bytes for a full packet
    #         data = self.serial_port.read(17)  # Read 17 bytes (size of your packet)
            
    #         # Unpack the data
    #         identifier = data[0]
    #         float_values = struct.unpack('<ffff', data[1:])
            
    #         print(f"Received: Identifier={identifier}, Float values={float_values}")
    
    # def send_data(self):
    #     data = 3.14159   # Example float data (replace with your actual float value)
    #     identifier = 32 
    #     telegram = struct.pack('>fB', data, identifier)
    #     print(telegram)
    #     done = self.serial_port.write(telegram)
    #     print(done)

          