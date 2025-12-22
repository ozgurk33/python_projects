from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt6.QtGui import QPixmap, QPainter, QPen, QColor
from PyQt6.QtCore import Qt
import sys


class main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setMinimumSize(400, 400)
    
    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)

        pen = QPen(QColor('#ebe834'), 5)
        painter.setPen(pen)

        painter.drawPoint(100, 100)
        painter.drawLine(0, 0, 100, 100)
        painter.drawRect(100, 100, 200, 200)
        painter.drawEllipse(100, 100, 200, 200)

        painter.end()


app = QApplication(sys.argv)
window = main_window()
window.show()
app.exec()
