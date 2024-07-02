from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QTimer

from window_ui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        # Load and set the converted ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Initialize components
        self.timer = QTimer(self)
        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.menu_button_1.setChecked(True)
        
        self.timer.timeout.connect(self.clear_temporary_message)
        self.set_temporary_message("Welcome to GITSIM!")

    def set_temporary_message(self, message:str, duration=3000):
        self.ui.temporary_message_label.setText(message)
        self.timer.start(duration) 
        print("start")

    def clear_temporary_message(self):
        self.ui.temporary_message_label.clear()
        print("Done")
        self.timer.stop()
    