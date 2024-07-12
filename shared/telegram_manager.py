from PySide6.QtSerialPort import QSerialPort
from PySide6.QtCore import Signal, QTimer 
import struct

class TelegramManager(QSerialPort):
    
    telegram_received = Signal()
    unknown_board_detected = Signal()
    
    def __init__(self):
        super().__init__()
        
        # Initialize default telegram
        self.assign_empty_telegram()
        self.board_identifier_timer = QTimer()
        
        self.last_data_received = {
            "speed1": float(0),
            "speed2": float(0),
            "cont1": int(0),
            "cont2": int(0),
        }
        self.setBaudRate(115200)
        self.readyRead.connect(self.read_response_telegram)
        self.board_identifier_timer.timeout.connect(self.emit_unknown_board)
        
    def emit_unknown_board(self):
        self.unknown_board_detected.emit()
        self.board_identifier_timer.stop()
    
    def read_response_telegram(self):
        
        if self.bytesAvailable() >= 12: 
            
            # Read and unpack
            uart_byte_array = self.read(12)
            uart_data = struct.unpack('<ffHH', uart_byte_array)
            
            # Update speed
            self.last_data_received["speed1"] =  uart_data[0]
            self.last_data_received["speed2"]  =  uart_data[1]
            
            # Update count
            self.last_data_received["count1"]  =  uart_data[2]
            self.last_data_received["count2"]  =  uart_data[3]
            
            # Send a functioning telegram in responce
            if self.check_responce_data():
                self.send_functioning_telegram()
                self.board_identifier_timer.stop()
                self.telegram_received.emit()
            
        
    def send_functioning_telegram(self) -> None:
        """
        Sends a functioning telegram to the board.
        If no special data has been assigned, the telegram 
        is filled with empty data.
        """
        # Send the value-telegram and addon-telegram
        self.write(self.value_telegram)
        self.write(self.addon_telegram)
        
        # Set the next telegram as empty
        self.assign_empty_telegram()
            
    def send_connection_telegram(self, diameter: float, 
                              ppr1: int, ppr2: int) -> None:
        """
        Sends the connection telegram via uart, formatted as wished 
        by the embedded application

        Args:
            diameter (float): diameter of wheel to emulate
            ppr1 (int): pulses per revolution of the 1st encoder
            ppr2 (int): pulses per revolution of the 2nd encoder
        """
        
        # Create "little endian" telegram
        telegram = struct.pack('<fHH',  diameter,
                                        ppr1, 
                                        ppr2)
        
        # Start a countdown in which the board has to respond
        self.board_identifier_timer.start(100)
        
        # Send telegram
        self.write(telegram)
        
    def assign_value_telegram(self, type: str, value1: float, 
                              value2: float):
        match type.upper():
            case "SPEED":
                self.assign_speed_telegram(value1, value2)
            case "ACCELERATION":
                self.assign_acceleration_telegram(value1, value2)
            case "DISCONNECTION":
                self.assign_disconnection_telegram()
            case _:
                msg = "Trying to send an unknown type of value-telegram"
                raise Exception(msg) 
    
    def assign_speed_telegram(self, speed1: float, speed2: float):
        identifier = int(1)
        self.value_telegram = struct.pack('<ffB', speed1, speed2, identifier)
        
    def assign_acceleration_telegram(self, acc1: float, acc2: float):
        identifier = int(2)
        self.value_telegram = struct.pack('<ffB', acc1, acc2, identifier)
    
    def assign_disconnection_telegram(self):
        identifier = int(3)
        self.value_telegram = struct.pack('<ffB', 0, 0, identifier)
        
    def assign_empty_telegram(self):
        self.value_telegram = struct.pack('<ffB', 0, 0, 0)
        self.addon_telegram = struct.pack('<fB', 0, 0)
        
    def check_responce_data(self) -> bool:
        
        # Check speed 1
        if self.last_data_received["speed1"] < 49.9:
            return False
        if self.last_data_received["speed1"] > 50.1:
            return False
        
        # Check speed 2
        if self.last_data_received["speed2"] < 49.9:
            return False
        if self.last_data_received["speed2"] > 50.1:
            return False
        
        # Check count 1
        if self.last_data_received["count1"] < 0:
            return False
        if self.last_data_received["count1"] > 4000:
            return False
        
        # Check count 2
        if self.last_data_received["count2"] < 0:
            return False
        if self.last_data_received["count2"] > 4000:
            return False
        
        return True
        
        
        