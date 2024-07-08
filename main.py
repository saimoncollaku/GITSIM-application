# Public libraries
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtSerialPort import QSerialPort

# Private libraries
from tabs.shared.mainwindow_class import MainWindow
from tabs.home.serial_box_home import SerialBox
from tabs.measurement.encoder_meas_box_measurement import EncoderMeasurementBox
    
if __name__ == "__main__":
    
    # Initialize shared resources
    app = QApplication(sys.argv)
    serial_port = QSerialPort()
    window = MainWindow()
    
    # Loading style file
    with open("style.qss", "r") as style_file:
        style_str = style_file.read()
    app.setStyleSheet(style_str)
    
    # Single resources modules
    serial_tab = SerialBox(window, serial_port)
    encoder_measure_box = EncoderMeasurementBox(window, serial_port)
    
    # UI loop
    window.show()

    sys.exit(app.exec())