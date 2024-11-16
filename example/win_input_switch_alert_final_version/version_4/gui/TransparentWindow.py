
from PyQt5.QtCore import QRectF, Qt
from PyQt5.QtGui import QColor, QPainter, QPainterPath, QRegion, QPen
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QGraphicsDropShadowEffect

# from config.GuiConfig import GUIConfig
# from config.KeypadConfig import KeyboardConfig


class TransparentWindow(QWidget):
    """ 透明窗口 """
    # global gui_opacity, gui_width, gui_height, gui_font, gui_font_size, gui_border_radius, gui_bg_color_r, gui_bg_color_g, gui_bg_color_b

    # gui_config = GUIConfig()

    # # 不透明度
    # gui_opacity = gui_config.get_gui_opacity()
    # # 窗口宽度
    # gui_width = gui_config.get_gui_width()
    # # 窗口高度
    # gui_height = gui_config.get_gui_height()
    # # 窗口字体
    # gui_font = gui_config.get_gui_font()
    # # 窗口字体大小
    # gui_font_size = gui_config.get_gui_font_size()
    # # 圆角
    # gui_border_radius = gui_config.get_gui_border_radius()
    # # 窗口背景颜色 - R
    # gui_bg_color_r = gui_config.get_bg_color_r()
    # # 窗口背景颜色 - G
    # gui_bg_color_g = gui_config.get_bg_color_g()
    # # 窗口背景颜色 - B
    # gui_bg_color_b = gui_config.get_bg_color_b()

    # def __init__(self, text, color=QColor(gui_bg_color_r, gui_bg_color_g, gui_bg_color_b), opacity=gui_opacity):
    def __init__(self, text, color=QColor(255, 255, 255), opacity=0.7):
        super().__init__()

        self.setWindowOpacity(opacity)
        self.setWindowFlags(Qt.FramelessWindowHint |
                            Qt.Tool | Qt.WindowStaysOnTopHint)

        # window_width, window_height = gui_width, gui_height
        window_width, window_height = 140, 110
        screen = QApplication.primaryScreen().geometry()
        x = (screen.width() - window_width) // 2
        y = screen.height() // 100
        self.setGeometry(x, y, window_width, window_height)

        label = QLabel(text, self)
        label.setStyleSheet(
            # f"font: {gui_font_size}pt '{gui_font}'; font-weight: bold;")
            f"font: 50pt '黑体'; font-weight: bold;")
        label.setAlignment(Qt.AlignCenter)
        label.setGeometry(0, 0, window_width, window_height)
        
        self.color = color
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(self.color)
        painter.setPen(Qt.transparent)

        # 圆角半径
        # radius = gui_border_radius
        radius = 20
        rectf = QRectF(self.rect())
        path = QPainterPath()
        path.addRoundedRect(rectf, radius, radius)

        region = QRegion(path.toFillPolygon().toPolygon())
        self.setMask(region)

        painter.fillPath(path, QColor(self.color.red(),
                         self.color.green(), self.color.blue(), 100))

        painter.end()
