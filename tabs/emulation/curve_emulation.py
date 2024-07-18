# Public libraries
from PySide6.QtWidgets import QFileDialog

import pandas as pd
import os
import numpy as np

# Private libraries
from shared.mainwindow import MainWindow
from shared.telegram_manager import TelegramManager
from shared.encoder_data import EncoderData

class CurveEmulation():
    def __init__(self, main_window: MainWindow, 
                    manager: TelegramManager,
                    encoder: EncoderData):
        
        # Setup shared resources
        self.main_window = main_window
        self.manager = manager
        self.encoder = encoder
        
        # Setup exclusive resources
        self.choose_file_button = self.main_window.ui.pushButton_4
        
        # Variables for file reading 
        self.data_frame = None
        self.curve_data = None
        
        # Setup signal connections
        self.choose_file_button.clicked.connect(self.load_emulation_file)
        
        
        
    def load_emulation_file(self):
        
        file_path = self.open_choose_file_dialog()
        
        if file_path != None:
                
                # Try to get access to the file
                file_extension = os.path.splitext(file_path)[1].lower()
                
                try:
                    if not self.check_file_extension(file_path, file_extension):
                        print(f"Unsupported file type")
                        return
                    
                    if not self.check_number_of_columns():
                        print(f"File should have exactly 2 columns.")
                        return
                    
                    if not self.check_values_are_numeric():
                        print("All values in the file should be numeric.")
                        return
                    
                    # Convert to numpy array of float64
                    self.data = self.data_frame.astype(float).to_numpy()
                    
                    file_name = os.path.basename(file_path)
                    # Do something with the data
                    print(f"Loaded file: {file_name}")
                    print(f"Number of rows: {self.data.shape[0]}")
                    print(f"First row: {self.data[0] if self.data.size else 'Empty file'}")
                    return
                
                except Exception:
                    print(f"Error reading file")
                    return            

    def check_values_are_numeric(self) -> bool:
        # Attempt to convert all columns to numeric
        numeric_df = self.data_frame.apply(pd.to_numeric, errors='coerce')
        
        # Check if any null values were introduced 
        return not numeric_df.isnull().any().any()
    
    def check_file_extension(self, path: str, extension: str) -> bool:
        if extension in ['.xlsx', '.xls']:
            self.data_frame = pd.read_excel(path, header=None)
            return True
        elif extension == '.csv':
            self.data_frame = pd.read_csv(path, header=None)
            return True
        return False
                    
    def check_number_of_columns(self) -> bool:
        if self.data_frame.shape[1] == 2:
            return True
        else:
            return False
    
    def open_choose_file_dialog(self) -> str:
        """Opens the dialog window, where its possible to choose 
        csv/xlsx/xls file types

        Returns:
            str: the chosen file filepath, returns 'None' if nothing is chosen
        """
        window_name = "Choose emulation file"
        file_types = ["Excel Files (*.xlsx *.xls)",
                    'CSV Files (*.csv)']
        permitted_file_types = ";;".join(file_types)
        
        # Open file dialog
        file_dialog = QFileDialog(None, window_name, "", permitted_file_types)
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        
        if file_dialog.exec() == QFileDialog.DialogCode.Accepted:
            # Pick only the first selected file
            file_path = file_dialog.selectedFiles()[0]
            return file_path
        else:
            return None
            