import sys
from PySide6.QtWidgets import QApplication

from mainwindow_class import MainWindow

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()
        
#         # Load style sheet file
#         with open("style.qss", "r") as style_file:
#             style_str = style_file.read()
#         app.setStyleSheet(style_str)
        
#         # Load and set the converted ui
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
        
#         # Initialize components
#         self.ui.icon_only_widget.hide()
#         self.ui.stackedWidget.setCurrentIndex(0)
#         self.ui.menu_button_1.setChecked(True)
    
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # loading style file
    with open("style.qss", "r") as style_file:
        style_str = style_file.read()
    app.setStyleSheet(style_str)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())