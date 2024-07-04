from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor, QPen, QFont, QPolygon
from PySide6.QtCore import Qt, QRectF, QPointF
import math

class GaugeMeter(QWidget):
    def __init__(self, parent=None, min_value=0, max_value=100, 
                 tick_interval=10):
        # Initialize the GaugeMeter widget
        super().__init__(parent)
        self.min_value = min_value
        self.max_value = max_value
        self.tick_interval = tick_interval
        self.value = min_value
        # self.setMinimumSize(200, 200)  # Set minimum size for the widget

    def set_value(self, value):
        # Set the current value of the gauge, ensuring it's within the valid range
        self.value = max(self.min_value, min(self.max_value, value))
        
        # Trigger the 
        self.update()

    def paintEvent(self, event):
        # Main paint event handler
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        rect = self.rect()
        center = rect.center()
        radius = min(rect.width(), rect.height()) / 2 - 10  # Reduced margin to 5

        # Draw various components of the gauge
        self.draw_background(painter, center, radius)
        self.draw_all_ticks(painter, center, radius)
        self.draw_arrow(painter, center, radius)
        self.draw_circle(painter, center)
        self.draw_value_label(painter, center, radius)  # Changed this line

    def draw_background(self, painter, center, radius):
        # Draw the circular background of the gauge
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(240, 240, 240))
        painter.drawEllipse(center, radius, radius)

    def draw_all_ticks(self, painter, center, radius):
        # Draw all tick marks and their labels
        painter.setPen(QPen(QColor(80, 80, 80), 2))
        painter.setFont(QFont("Arial", 8))
        
        num_ticks = int((self.max_value - self.min_value) / self.tick_interval) + 1
        
        for i in range(num_ticks):
            self.draw_tick(painter, center, radius, i)

    def draw_tick(self, painter, center, radius, tick_index):
        # Draw a single tick mark and its label
        tick_value = self.min_value + tick_index * self.tick_interval
        angle = self.value_to_angle(tick_value)
        sin_angle = math.sin(math.radians(angle))
        cos_angle = math.cos(math.radians(angle))
        
        # Calculate positions for the tick mark
        outer_point = QPointF(center.x() + (radius - 5) * cos_angle,
                              center.y() - (radius - 5) * sin_angle)
        inner_point = QPointF(center.x() + (radius - 15) * cos_angle,
                              center.y() - (radius - 15) * sin_angle)
        
        # Draw the tick mark
        painter.drawLine(outer_point, inner_point)
        
        # Draw the label for the tick mark
        label_point = QPointF(center.x() + (radius - 30) * cos_angle,
                              center.y() - (radius - 30) * sin_angle)
        painter.drawText(label_point.x() - 10, label_point.y() + 5, 
                         str(tick_value))

    def draw_arrow(self, painter, center, radius):
        # Draw the arrow indicator
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(255, 0, 0))
        
        arrow_angle = self.value_to_angle(self.value)
        arrow_length = radius - 20
        arrow_width = 8
        
        # Calculate arrow points
        arrow_head = self.calculate_arrow_point(center, arrow_length, 
                                                arrow_angle)
        arrow_base_left = self.calculate_arrow_point(center, arrow_width/2, 
                                                     arrow_angle + 90)
        arrow_base_right = self.calculate_arrow_point(center, arrow_width/2, 
                                                      arrow_angle - 90)
        
        # Create and draw the arrow polygon
        arrow = QPolygon([
            arrow_head.toPoint(),
            arrow_base_left.toPoint(),
            arrow_base_right.toPoint()
        ])
        
        painter.drawPolygon(arrow)

    def calculate_arrow_point(self, center, length, angle):
        # Calculate a point on the circumference given center, length and angle
        return QPointF(
            center.x() + length * math.cos(math.radians(angle)),
            center.y() - length * math.sin(math.radians(angle))
        )

    def draw_circle(self, painter, center):
        # Draw the central circle of the gauge
        painter.setBrush(QColor(120, 120, 120))
        painter.drawEllipse(center, 10, 10)

    def draw_value_label(self, painter, center, radius):
        # Draw the current value label at the bottom inside the gauge circle
        painter.setPen(QColor(0, 0, 0))
        painter.setFont(QFont("Arial", 10, QFont.Bold))
        value_text = f"{self.value:.2f} ㎧"
        
        # Calculate the position for the text
        text_width = painter.fontMetrics().horizontalAdvance(value_text)
        text_height = painter.fontMetrics().height()
        
        # Position the text at the bottom inside the circle
        text_x = center.x() - text_width / 2
        text_y = center.y() + radius - text_height - 5  # 5 pixels padding from bottom
        
        painter.drawText(text_x, text_y, value_text)

    def value_to_angle(self, value):
        # Convert a value to its corresponding angle on the gauge
        return 225 - (value - self.min_value) * (270 / (self.max_value - self.min_value))
