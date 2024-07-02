import sys
from PySide6.QtWidgets import QApplication

from mainwindow_class import MainWindow
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # loading style file
    with open("style.qss", "r") as style_file:
        style_str = style_file.read()
    app.setStyleSheet(style_str)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())