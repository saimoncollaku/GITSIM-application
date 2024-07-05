# Public libraries
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtSerialPort import QSerialPort

# Private libraries
from classes.mainwindow.mainwindow_class import MainWindow
from classes.home.serialbox_class import SerialBox
    
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
    
    
    # UI loop
    window.show()

    sys.exit(app.exec())