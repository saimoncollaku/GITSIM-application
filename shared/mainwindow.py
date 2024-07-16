
# Public libraries
from PySide6.QtWidgets import QMainWindow, QPushButton
from PySide6.QtCore import QTimer
from PySide6.QtGui import QMovie
from PySide6.QtGui import QFontDatabase

# Private libraries
from ui.window_ui import Ui_MainWindow

def setup_gif_button(button: QPushButton, gif_path):
    movie = QMovie(gif_path)
    button.movie = movie  # Store the movie as an attribute of the button
    
    button.setCheckable(True)
    button.toggled.connect(button.on_toggle)

def toggle_gif(button: QPushButton, checked):
    if checked:
        button.movie.start()
        button.setIcon(button.movie.currentPixmap())
        button.movie.updated.connect(button.update_icon)
    else:
        button.movie.stop()
        button.setIcon(button.movie.currentPixmap())
        button.movie.updated.disconnect(button.update_icon)

def update_button_icon(button: QPushButton):
    button.setIcon(button.movie.currentPixmap())

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        # Load and set the converted ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # # Apply custom font
        font_path = "font\\7segment\\7segment.ttf"
        QFontDatabase.addApplicationFont(font_path)
        
        # Initialize components
        self.timer = QTimer(self)
        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.menu_button_1.setChecked(True)
        self.ui.connection_button_1.setChecked(True)
        self.timer.timeout.connect(self.clear_temporary_message)
        self.set_temporary_message("Welcome to GITSIM!")
        self.setup_tab_changes()
        self.single_value_to_disabled()
        

    def set_temporary_message(self, message:str, duration:int=3000):
        self.ui.temporary_message_label.setText(message)
        self.ui.temporary_message_label.setStyleSheet("background-color: #ece635;")
        self.timer.start(duration) 

    def clear_temporary_message(self):
        self.ui.temporary_message_label.clear()
        self.ui.temporary_message_label.setStyleSheet("")
        self.timer.stop()
        
    def setup_tab_changes(self):
        # Set slots to change the pages - Page 0
        self.ui.connection_button_1.clicked.connect(self.set_connection_tab)
        self.ui.connection_button_2.clicked.connect(self.set_connection_tab)
        # Set slots to change the pages - Page 1
        self.ui.measurement_button_1.clicked.connect(self.set_measurement_tab)
        self.ui.measurement_button_2.clicked.connect(self.set_measurement_tab)
        # Set slots to change the pages - Page 2
        self.ui.curve_button_1.clicked.connect(self.set_curve_tab)
        self.ui.curve_button_2.clicked.connect(self.set_curve_tab)
        # Set slots to change the pages - Page 3
        self.ui.error1_button_1.clicked.connect(self.set_error1_tab)
        self.ui.error1_button_2.clicked.connect(self.set_error1_tab)
        # Set slots to change the pages - Page 4
        self.ui.error2_button_1.clicked.connect(self.set_error2_tab)
        self.ui.error2_button_2.clicked.connect(self.set_error2_tab)
        
        
    def set_permanent_message(self, message:str):
        self.ui.permanent_message_label.setText(message)
    
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
        
    def serial_box_interface_to_connected(self):
        self.ui.com_connect_button.setEnabled(False)
        self.ui.com_disconnect_button.setEnabled(True)
        self.ui.ppr1_spinbox.setEnabled(False)
        self.ui.ppr2_spinbox.setEnabled(False)
        self.ui.diameter_spinbox.setEnabled(False)
        
    def serial_box_interface_to_disconnected(self):
        self.ui.com_connect_button.setEnabled(True)
        self.ui.com_disconnect_button.setEnabled(False)
        self.ui.ppr1_spinbox.setEnabled(True)
        self.ui.ppr2_spinbox.setEnabled(True)
        self.ui.diameter_spinbox.setEnabled(True)
        
    def serial_box_interface_to_disabled(self):
        self.ui.com_connect_button.setEnabled(False)
        self.ui.com_disconnect_button.setEnabled(False)
        self.ui.ppr1_spinbox.setEnabled(False)
        self.ui.ppr2_spinbox.setEnabled(False)
        self.ui.diameter_spinbox.setEnabled(False)    
        
    def single_value_to_disabled(self):
        self.ui.speed_spinbox.setEnabled(False)
        self.ui.acc_spinbox.setEnabled(False)
        self.ui.set_speed_button.setEnabled(False)
        self.ui.set_acc_button.setEnabled(False)
        self.ui.single_both_radio.setEnabled(False)
        self.ui.single_encoder1_radio.setEnabled(False)
        self.ui.single_encoder2_radio.setEnabled(False)
        
    def single_value_to_enabled(self):
        self.ui.speed_spinbox.setEnabled(True)
        self.ui.acc_spinbox.setEnabled(True)
        self.ui.set_speed_button.setEnabled(True)
        self.ui.set_acc_button.setEnabled(True)
        self.ui.single_both_radio.setEnabled(True)
        self.ui.single_encoder1_radio.setEnabled(True)
        self.ui.single_encoder2_radio.setEnabled(True)