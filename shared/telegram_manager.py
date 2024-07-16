from PySide6.QtSerialPort import QSerialPort
from PySide6.QtCore import QEventLoop
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
        # self.connection_is = False
        
        
    def emit_unknown_board(self):
        self.unknown_board_detected.emit()
        self.board_identifier_timer.stop()
        self.clear(QSerialPort.Direction.Input)
        self.close()
        self.setPortName("") 
    
    
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
            
            if not self.board_identifier_timer.isActive():
                print("ok")
                self.send_functioning_telegram()
                self.telegram_received.emit()
                return
            
            # Send a functioning telegram in responce
            # print(self.check_responce_data())
            if self.check_responce_data():
                print("taaak")
                self.send_functioning_telegram()
                self.board_identifier_timer.stop()
                self.telegram_received.emit()
                return
                
            
        
    def send_functioning_telegram(self) -> None:
        """
        Sends a functioning telegram to the board.
        If no special data has been assigned, the telegram 
        is filled with empty data.
        """
        # Send the value-telegram and addon-telegram
        self.write(self.value_telegram)
        self.write(self.addon_telegram)
        print(self.value_telegram)
        if self.value_telegram[8] == 3:
            self.close_serial_connection()
            
        
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
        self.board_identifier_timer.start(150)
        # self.connection_is = True
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
            print("1")
            return False
        elif self.last_data_received["speed1"] > 50.1:
            print("2")
            return False
        
        # Check speed 2
        if self.last_data_received["speed2"] < 49.9:
            print("3")
            return False
        elif self.last_data_received["speed2"] > 50.1:
            print("4")
            return False
        
        return True
   
   
    def close_serial_connection(self):
        # Force write (its not enough)
        self.flush()
        
        # Clean input buffer
        self.clear(QSerialPort.Direction.Input)
        
        # Loop to make the computer uart controller write 
        # every byte, it's the only implementation that I made
        # which 100% works
        # TODO find a more simple implementation
        if self.bytesToWrite() > 0:
            
            def check_bytes_written():
                if self.bytesToWrite() == 0:
                    loop.quit()
            
            loop = QEventLoop()
            timeout_timer = QTimer()
            check_timer = QTimer()
            timeout_timer.setSingleShot(True)
            timeout_timer.timeout.connect(loop.quit)
            check_timer.timeout.connect(check_bytes_written)
            
            check_timer.start(5)
            timeout_timer.start(50)
            loop.exec()
            check_timer.stop()
                
        self.close()
        self.setPortName("")
        
        