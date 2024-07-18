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
        
        # Setup signal connections
        self.choose_file_button.clicked.connect(self.load_emulation_file)
        
        
    def load_emulation_file(self):
        # window_name = "Choose emulation file"
        # file_types = ["Excel Files (*.xlsx *.xls)",
        #             'CSV Files (*.csv)']
        # permitted_file_types = ";;".join(file_types)
        
        # # Open file dialog
        # file_dialog = QFileDialog(None, window_name, "", permitted_file_types)
        # file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        file_path = self.open_choose_file_dialog()
        
        if file_path != None:
                
                # Try to get access to the file
                file_extension = os.path.splitext(file_path)[1].lower()
                
                try:
                    # Read the file
                    if file_extension in ['.xlsx', '.xls']:
                        df = pd.read_excel(file_path, header=None)
                    elif file_extension == '.csv':
                        df = pd.read_csv(file_path, header=None)
                    else:
                        print(f"Unsupported file type: {file_extension}")
                        return None
                    
                    # Check if file has exactly 2 columns
                    if df.shape[1] != 2:
                        print(f"File should have exactly 2 columns. Found {df.shape[1]} columns.")
                        return None
                    
                    # Check if all values are numeric
                    if not self.are_all_values_numeric(df):
                        print("All values in the file should be numeric.")
                        return None
                    
                    # Convert to numpy array of float64
                    data = df.astype(float).to_numpy()
                    
                    # Do something with the data
                    print(f"Loaded file: {file_path}")
                    print(f"Number of rows: {data.shape[0]}")
                    print(f"First row: {data[0] if data.size else 'Empty file'}")
                    
                    return data
                
                except Exception:
                    print(f"Error reading file")
                    return None
                

    def are_all_values_numeric(self, df):
        # Attempt to convert all columns to numeric
        numeric_df = df.apply(pd.to_numeric, errors='coerce')
        
        # Check if any null values were introduced 
        return not numeric_df.isnull().any().any()
    
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
        