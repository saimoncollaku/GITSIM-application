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
        self.ui.connection_button_1.setChecked(True)
        
        self.timer.timeout.connect(self.clear_temporary_message)
        self.set_temporary_message("Welcome to GITSIM!")
        self.ui.connection_button_1.clicked.connect(self.set_connection_tab)
        self.ui.connection_button_2.clicked.connect(self.set_connection_tab)
        
        self.ui.measurement_button_1.clicked.connect(self.set_measurement_tab)
        self.ui.measurement_button_2.clicked.connect(self.set_measurement_tab)
        
        self.ui.curve_button_1.clicked.connect(self.set_curve_tab)
        self.ui.curve_button_2.clicked.connect(self.set_curve_tab)
        
        self.ui.error1_button_1.clicked.connect(self.set_error1_tab)
        self.ui.error1_button_2.clicked.connect(self.set_error1_tab)
        
        self.ui.error2_button_1.clicked.connect(self.set_error2_tab)
        self.ui.error2_button_2.clicked.connect(self.set_error2_tab)
        

    def set_temporary_message(self, message:str, duration:int=3000):
        self.ui.temporary_message_label.setText(message)
        self.ui.temporary_message_label.setStyleSheet("background-color: #ece635;")
        self.timer.start(duration) 
        print("start")

    def clear_temporary_message(self):
        self.ui.temporary_message_label.clear()
        self.ui.temporary_message_label.setStyleSheet("")
        print("Done")
        self.timer.stop()
    
    def set_connection_tab(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    
    def set_measurement_tab(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        
    def set_curve_tab(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        
    def set_error1_tab(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        
    def set_error2_tab(self):
        self.ui.stackedWidget.setCurrentIndex(4)