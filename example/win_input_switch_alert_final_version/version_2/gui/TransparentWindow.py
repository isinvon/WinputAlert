# from PyQt5.QtCore import QRectF, Qt
# from PyQt5.QtGui import QColor, QPainter, QPainterPath, QRegion
# from PyQt5.QtWidgets import QApplication, QLabel, QWidget

# class TransparentWindow(QWidget):
#     def __init__(self, text, color=QColor(255, 255, 255), opacity=0.3):
#         super().__init__()

#         self.setWindowOpacity(opacity)
#         self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)
        
#         window_width, window_height = 110, 90
#         screen = QApplication.primaryScreen().geometry()
#         x = (screen.width() - window_width) // 2
#         y = screen.height() // 80
#         self.setGeometry(x, y, window_width, window_height)

#         label = QLabel(text, self)
#         label.setStyleSheet("font: 40pt '黑体'; font-weight: bold;")
#         label.setAlignment(Qt.AlignCenter)
#         label.setGeometry(0, 0, window_width, window_height)

#         self.color = color
#         self.show()

#     def paintEvent(self, event):
#         painter = QPainter(self)
#         path = QPainterPath()
#         path.addRect(0, 0, self.width(), self.height())
#         painter.setClipPath(path)
#         painter.setBrush(self.color)
#         painter.drawRect(0, 0, self.width(), self.height())
#         painter.end()
# gui/TransparentWindow.py
from PyQt5.QtCore import QRectF, Qt
from PyQt5.QtGui import QColor, QPainter, QPainterPath, QRegion
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

class TransparentWindow(QWidget):
    def __init__(self, text, color=QColor(255, 255, 255), opacity=0.5):
        super().__init__()

        self.setWindowOpacity(opacity)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)
        
        window_width, window_height = 150, 100
        screen = QApplication.primaryScreen().geometry()
        x = (screen.width() - window_width) // 2
        y = screen.height() // 80
        self.setGeometry(x, y, window_width, window_height)

        label = QLabel(text, self)
        label.setStyleSheet("font: 50pt '黑体'; font-weight: bold;")
        label.setAlignment(Qt.AlignCenter)
        label.setGeometry(0, 0, window_width, window_height)

        self.color = color
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(self.color)
        painter.setPen(Qt.transparent)
        
        radius = 20
        rectf = QRectF(self.rect())
        path = QPainterPath()
        path.addRoundedRect(rectf, radius, radius)
        
        region = QRegion(path.toFillPolygon().toPolygon())
        self.setMask(region)
        
        painter.fillPath(path, QColor(self.color.red(), self.color.green(), self.color.blue(), 100))
        painter.end()
