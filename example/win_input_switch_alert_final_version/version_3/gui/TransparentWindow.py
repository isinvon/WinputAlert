
from PyQt5.QtCore import QRectF, Qt
from PyQt5.QtGui import QColor, QPainter, QPainterPath, QRegion
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

from config.GuiConfig import GUIConfig


# 获取gui配置
gui = GUIConfig()
# 获取不透明度
gui_opacity =  gui.get_gui_opacity()
# 获取高度
gui_height = gui.get_gui_height()
# 获取宽度
gui_width = gui.get_gui_width()
# 获取字体大小
gui_font_size = gui.get_gui_font_size()
# 获取字体颜色
gui_font_color = gui.get_gui_font_color()
# 获取字体
gui_font = gui.get_gui_font()
# 获取圆角
gui_radius = gui.get_gui_border_radius()


class TransparentWindow(QWidget):
    def __init__(self, text, color=QColor(255, 255, 255), opacity=gui_opacity):
        super().__init__()

        self.setWindowOpacity(opacity)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)
        
        window_width, window_height = gui_width, gui_height
        screen = QApplication.primaryScreen().geometry()
        x = (screen.width() - window_width) // 2
        y = screen.height() // 80
        self.setGeometry(x, y, window_width, window_height)

        label = QLabel(text, self)
        label.setStyleSheet(f"font: {gui_font_size}pt '{gui_font}'; font-weight: bold;")
        label.setAlignment(Qt.AlignCenter)
        label.setGeometry(0, 0, window_width, window_height)

        self.color = color
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(self.color)
        painter.setPen(Qt.transparent)
        
        radius = gui_radius
        rectf = QRectF(self.rect())
        path = QPainterPath()
        path.addRoundedRect(rectf, radius, radius)
        
        region = QRegion(path.toFillPolygon().toPolygon())
        self.setMask(region)
        
        painter.fillPath(path, QColor(self.color.red(), self.color.green(), self.color.blue(), 100))
        painter.end()
