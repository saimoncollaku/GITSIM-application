# Public libraries
from PySide6.QtSerialPort import QSerialPort
import struct
import math

# Private libraries
from classes.mainwindow.mainwindow_class import MainWindow

class EncoderMeasurementBox:
    def __init__(self, main_window: MainWindow, serial_port: QSerialPort):
        # Setup shared resources
        self.main_window = main_window
        self.serial_port = serial_port
        
        # Setup exclusive resources
        self.distance1_label = main_window.ui.distance_encoder1_label
        self.distance1_label = main_window.ui.distance_encoder2_label
        
        # Set speed for Encoder
        self.speed_encoder1 = 0
        self.speed_encoder2 = 0
        
        # Set distance for Encoder
        self.distance_encoder1 = 0
        self.distance_encoder2 = 0
        
        self.serial_port.readyRead.connect(self.read_data)
        
        

    def read_data(self):
        # if self.serial_port.bytesAvailable() < 12:
            
            
        # Ensure we have enough bytes for a full packet
        if self.serial_port.bytesAvailable() >= 12: 
            # Read 12 bytes (size of your packet) 
            uart_byte_array = self.serial_port.read(12) 
            
            # Unpack the data (little endian)
            uart_data = struct.unpack('<ffHH', uart_byte_array)
            
            self.update_measurement(uart_data)
            
            
            
    def update_measurement(self, uart_data):
        # Set speed
        self.speed_encoder1 =  uart_data[0]
        self.speed_encoder2 =  uart_data[1]
         
        # Set space
        distance = uart_data[2]
        self.distance_encoder1 +=  uart_data[2]
        self.distance_encoder2 +=  uart_data[3]
        
    def display_measurement(self):
        
        self.distance1_label.setText(f"")
        
        
