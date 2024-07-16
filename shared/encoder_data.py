from PySide6.QtCore import Signal, QObject

class EncoderData(QObject):
    variables_updated = Signal()
    costants_updated = Signal()
    
    def __init__(self):
        super().__init__()
        
        # Costants
        self.diameter = float(0)
        self.ppr_e1 = int(1)
        self.ppr_e2 = int(1)
        
        # Speed
        self.speed_e1 = float(0)
        self.speed_e2 = float(0)
        
        # Counters
        self.counter_e1 = int(0)
        self.counter_e2 = int(0)
        
    def update_speed_and_count(self, speed1: int, speed2: int,
                                 count1: float, count2: float):
        self.counter_e1 += int(count1)
        self.counter_e2 += int(count2)
        self.speed_e1 = float(speed1)
        self.speed_e2 = float(speed2)
        self.variables_updated.emit()
        
    def update_costants(self, diameter: float, ppr1: int, ppr2: int):
        self.diameter = diameter
        self.ppr_e1 = ppr1
        self.ppr_e2 = ppr2
        self.costants_updated.emit()
        
    def reset_variables(self):
        self.counter_e1 = int(0)
        self.counter_e2 = int(0)
        self.speed_e1 = 0.00
        self.speed_e2 = 0.00
        self.variables_updated.emit()