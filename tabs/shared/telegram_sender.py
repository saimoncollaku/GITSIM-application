from PySide6.QtSerialPort import QSerialPort
import struct

class TelegramSender(QSerialPort):
    def __init__(self):
        super(QSerialPort, self).__init__()
        self.telegramma_da_mandare = None
        
    def manda_velocita(self, vel1: float, vel2: float):
        self.telegramma_da_mandare = "Velocita"
        
        