# Public imports
from PySide6.QtCore import Slot

# Private imports
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
        self.counter1_label = main_window.ui.pulses_encoder1_label
        self.counter2_label = main_window.ui.pulses_encoder2_label
        self.gauge_meter1 = main_window.ui.gauge_meter_1
        self.gauge_meter2 = main_window.ui.gauge_meter_2
        
        # Store the displayed values
        self.displayed_distance1 = 0
        self.displayed_distance2 = 0
        self.displayed_speed1 = 0
        self.displayed_speed2 = 0
        self.displayed_count1 = 0
        self.displayed_count2 = 0
        
        # Set up signals
        self.manager.telegram_received.connect(self.update_encoder_object)
        self.encoder.variables_updated.connect(self.update_measurements)
    
    @Slot()
    def update_encoder_object(self):
        speed1 = self.manager.last_data_received["speed1"]
        speed2 = self.manager.last_data_received["speed2"]
        count1 = self.manager.last_data_received["count1"]
        count2 = self.manager.last_data_received["count2"]
        self.encoder.update_speed_and_count(speed1, speed2, count1, count2)         
            
    def update_speed_measurement(self):
        if self.displayed_speed1 != self.encoder.speed_e1:
            self.displayed_speed1 = self.encoder.speed_e1
            self.gauge_meter1.set_value(self.displayed_speed1)
            
        if self.displayed_speed2 != self.encoder.speed_e2:
            self.displayed_speed2 = self.encoder.speed_e2
            self.gauge_meter2.set_value(self.displayed_speed2)
     
    def update_distance_measurement(self):
        if self.displayed_count1 != self.encoder.counter_e1:
            # Calculating the distance
            den = self.encoder.ppr_e1 * 4
            num = self.encoder.diameter * 3.14159
            self.displayed_distance1 = self.encoder.counter_e1 * num / den
            # Formatting the string in a nice way
            integer_part = f"{int(self.displayed_distance1):<2}"
            decimal_part = f"{self.displayed_distance1 % 1:.2f}"[1:]
            output_string = f"{integer_part}\u2009.\u2009{decimal_part[1:]}"
            self.distance1_label.setText(output_string)
            
        if self.displayed_count2 != self.encoder.counter_e2:
            # Calculating the distance
            den = self.encoder.ppr_e2 * 4 
            num = self.encoder.diameter * 3.14159
            self.displayed_distance2 = self.encoder.counter_e2 * num / den
            # Formatting the string in a nice way
            integer_part = f"{int(self.displayed_distance2):<2}"
            decimal_part = f"{self.displayed_distance2 % 1:.2f}"[1:]
            output_string = f"{integer_part}\u2009.\u2009{decimal_part[1:]}"
            self.distance2_label.setText(output_string)
            
    def update_counter_measurement(self):
        if self.displayed_count1 != self.encoder.counter_e1:
            self.displayed_count1 = self.encoder.counter_e1
            self.counter1_label.setText(f"{self.encoder.counter_e1}")
            
        if self.displayed_count2 != self.encoder.counter_e2:
            self.displayed_count2 = self.encoder.counter_e2
            self.counter2_label.setText(f"{self.encoder.counter_e2}")
    
    @Slot()     
    def update_measurements(self):
        self.update_distance_measurement()
        self.update_speed_measurement()
        self.update_counter_measurement()