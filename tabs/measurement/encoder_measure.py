# Public libraries
import struct
import math

# Private libraries
from shared.mainwindow import MainWindow
from shared.telegram_manager import TelegramManager
from shared.encoder_data import EncoderData

class EncoderMeasurementBox():
    def __init__(self, main_window: MainWindow, 
                 manager: TelegramManager,
                 encoder: EncoderData):
        # Setup shared resources
        self.main_window = main_window
        self.manager = manager
        self.encoder = encoder
        
        # Setup exclusive resources
        self.distance1_label = main_window.ui.distance_encoder1_label
        self.distance2_label = main_window.ui.distance_encoder2_label
        
        self.manager.telegram_received.connect(self.update_encoder_object)
        self.encoder.variables_updated.connect(self.update_measurements)
        
        
    def new_data_received(self):
        self.update_encoder_object()   
          
        
    def update_encoder_object(self):
        speed1 = self.manager.last_data_received["speed1"]
        speed2 = self.manager.last_data_received["speed2"]
        count1 = self.manager.last_data_received["count1"]
        count2 = self.manager.last_data_received["count2"]
        self.encoder.update_speed_and_count(speed1, speed2, count1, count2)         
            
        
    def update_speed_measurement(self, speed1: float, speed2: float):
        pass
    
        
    def update_distance_measurement(self, count1: int, count2: int):
        current_count1 = int(self.distance1_label)
        current_count2 = int(self.distance2_label)
        
        if current_count1 != self.encoder.counter_e1:
            self.distance1_label.setText(f"{self.encoder.counter_e1} m")
            
        if current_count2 != self.encoder.counter_e2:
            self.distance2_label.setText(f"{self.encoder.counter_e2} m")
            
                  
    def update_measurements(self):
        self.update_distance_measurement()
        self.update_speed_measurement()
        
        
