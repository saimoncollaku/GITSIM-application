# Public libraries
from PySide6 import QtCore
from PySide6.QtSerialPort import QSerialPortInfo, QSerialPort
import struct

# Private libraries
from classes.mainwindow.mainwindow_class import MainWindow

class EncoderMeasurementBox:
    def __init__(self, main_window: MainWindow, serial_port: QSerialPort):
        
        # Setup shared classes
        self.main_window = main_window
        self.serial_port = serial_port
        

    def read_data(self):
        # Ensure we have enough bytes for a full packet
        while self.serial_port.bytesAvailable() >= 12: 
            # Read 12 bytes (size of your packet) 
            data = self.serial_port.read(12) 
            
            # Unpack the data
            values = struct.unpack('<ffHH', data)
            
            print(f"{values}")
        
