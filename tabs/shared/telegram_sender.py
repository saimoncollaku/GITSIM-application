from PySide6.QtSerialPort import QSerialPort
import struct

class TelegramSender(QSerialPort):
    def __init__(self):
        super().__init__()
        
        # Initialize default telegram
        self.assign_empty_telegram()
        
        # Assign slot/signal
        self.readyRead.connect(self.send_functioning_telegram)
        
    def send_functioning_telegram(self) -> None:
        """
        Sends a functioning telegram to the board,
        after a responce has been received from the latter.
        If no special data has been assigned, the telegram 
        is filled with zeroes.
        """
        
        # Ensure the board sent a full packet
        if self.bytesAvailable() >= 12: 
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
        
        # Send telegram
        self.write(telegram)
        
    def assign_value_telegram(self, type: str, value1: float, value2: float):
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