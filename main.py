# Public imports
import sys
from PySide6.QtWidgets import QApplication

# Private imports (shared directory)
from shared.mainwindow import MainWindow
from shared.telegram_manager import TelegramManager
from shared.encoder_data import EncoderData
# 
# Private imports (tabs directory)
from tabs.home.serial_box import SerialBox

from tabs.measurement.encoder_measure import EncoderMeasurementBox
from tabs.measurement.set_single_value import SetSingleValue
from tabs.emulation.curve_emulation import CurveEmulation
    
if __name__ == "__main__":
    
    # Initialize shared resources
    app = QApplication(sys.argv)
    telegram_manager = TelegramManager()
    window = MainWindow()
    encoder_data = EncoderData()
    
    # Loading style file
    with open("style.qss", "r") as style_file:
        style_str = style_file.read()
    app.setStyleSheet(style_str)
    
    # Single resources modules
    serial_connection_tab = SerialBox(window, 
                                      telegram_manager, 
                                      encoder_data)
    encoder_measure_box = EncoderMeasurementBox(window, 
                                                telegram_manager,
                                                encoder_data)
    set_single_value_box = SetSingleValue(window, 
                                          telegram_manager, 
                                          encoder_data)
    curve_emulation_tab = CurveEmulation(window, 
                                          telegram_manager, 
                                          encoder_data)
    
    # UI loop
    window.show()

    sys.exit(app.exec())