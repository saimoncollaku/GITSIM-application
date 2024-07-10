# Public libraries
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtSerialPort import QSerialPort

# Private libraries
from tabs.shared.mainwindow import MainWindow
from tabs.home.serial_box import SerialBox
from tabs.measurement.encoder_measure import EncoderMeasurementBox
from tabs.shared.telegram_sender import TelegramSender
    
if __name__ == "__main__":
    
    # Initialize shared resources
    app = QApplication(sys.argv)
    sender = TelegramSender()
    window = MainWindow()
    
    # Loading style file
    with open("style.qss", "r") as style_file:
        style_str = style_file.read()
    app.setStyleSheet(style_str)
    
    # Single resources modules
    serial_tab = SerialBox(window, sender)
    encoder_measure_box = EncoderMeasurementBox(window, sender)
    
    # UI loop
    window.show()

    sys.exit(app.exec())