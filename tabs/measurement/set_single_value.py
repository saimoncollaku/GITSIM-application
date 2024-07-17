# Private libraries
from shared.mainwindow import MainWindow
from shared.telegram_manager import TelegramManager
from shared.encoder_data import EncoderData

class SetSingleValue():
    def __init__(self, main_window: MainWindow, 
                 manager: TelegramManager,
                 encoder: EncoderData):
        # Setup shared resources
        self.main_window = main_window
        self.manager = manager
        self.encoder = encoder
        
        # Blabla
        self.change_encoder1 = self.main_window.ui.single_encoder1_radio
        self.change_encoder2 = self.main_window.ui.single_encoder2_radio
        self.change_both = self.main_window.ui.single_both_radio
        self.speed_spinbox = self.main_window.ui.speed_spinbox
        self.acc_spinbox = self.main_window.ui.acc_spinbox
        self.set_speed_button = self.main_window.ui.set_speed_button
        self.set_acc_button = self.main_window.ui.set_acc_button
        
        self.set_speed_button.clicked.connect(self.call_uart_send_speed)
        self.set_acc_button.clicked.connect(self.call_uart_send_acceleration)
        self.manager.aboutToClose.connect(self.main_window.single_value_to_disabled)
        
    def return_encoder_to_modify(self) -> str:
        
        if self.change_encoder1.isChecked():
            return "1"
        elif self.change_encoder2.isChecked():
            return "2"
        elif self.change_both.isChecked():
            return "both"
        
        msg = "The app tried to change an unknow option"
        raise Exception(msg)
        
    def call_uart_send_speed(self):
        option = self.return_encoder_to_modify()
                
        if option == "1":
            self.manager.assign_speed_e1_telegram(self.speed_spinbox.value())
        elif option == "2":
            self.manager.assign_speed_e2_telegram(self.speed_spinbox.value())
        elif option == "both":
            self.manager.assign_speed_both_telegram(self.speed_spinbox.value(),
                                                    self.speed_spinbox.value())
            
    def call_uart_send_acceleration(self):
        option = self.return_encoder_to_modify()
                
        if option == "1":
            self.manager.assign_acc_e1_telegram(self.acc_spinbox.value())
        elif option == "2":
            self.manager.assign_acc_e2_telegram(self.acc_spinbox.value())
        elif option == "both":
            self.manager.assign_acc_both_telegram(self.acc_spinbox.value(),
                                                self.acc_spinbox.value())
             