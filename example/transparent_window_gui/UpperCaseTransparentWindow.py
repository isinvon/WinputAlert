from PyQt5.QtCore import QRectF, Qt  # type: ignore
from PyQt5.QtGui import QColor, QPainter, QPainterPath, QRegion  # type: ignore
from PyQt5.QtWidgets import QApplication, QLabel, QWidget  # type: ignore


class UpperCaseTransparentWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗口的透明度
        self.setWindowOpacity(0.3)

        # 去掉窗口的标题栏和边框
        self.setWindowFlags(Qt.FramelessWindowHint)

        # 设置窗口的宽高
        window_width = 110
        window_height = 90

        # 获取屏幕宽度和高度
        screen = QApplication.primaryScreen()
        screen_geometry = screen.geometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()

        # 计算窗口的左上角位置，使其水平居中并靠近顶部
        x = (screen_width - window_width) // 2
        y = screen_height // 80

        # 设置窗口的宽高和位置
        self.setGeometry(x, y, window_width, window_height)
        
        # 任务栏不出现图标
        self.setWindowFlags(Qt.Tool)
        
        # 设置窗口置顶
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)

        # 设置标签和字体
        label = QLabel('A', self)
        label.setStyleSheet("font: 40pt '黑体'; font-weight: bold;")  # 设置字体为粗体
        label.setAlignment(Qt.AlignCenter)  # 设置文字居中
        label.setGeometry(0, 0, window_width, window_height)

        # 显示窗口
        self.show()

    def paintEvent(self, event):
        """ 
        重写paintEvent方法，实现窗口的圆角效果
        """
        # 使用QPainter绘制圆角矩形
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # 启用抗锯齿，改善圆角效果
        painter.setBrush(QColor(255, 255, 255))  # 设置背景颜色（白色）
        painter.setPen(Qt.transparent)  # 不需要边框

        # 设置圆角半径
        radius = 20
        rect = self.rect()  # 获取窗口的矩形区域

        # 将QRect转为QRectF类型
        rectf = QRectF(rect)

        path = QPainterPath()
        path.addRoundedRect(rectf, radius, radius)  # 绘制圆角矩形

        # 应用蒙版，设置窗口的形状为圆角矩形
        region = QRegion(path.toFillPolygon().toPolygon())
        self.setMask(region)  # 将窗口的显示区域设为圆角矩形

        # 填充圆角矩形
        painter.fillPath(path, QColor(255, 255, 255, 100))  # 使用带透明度的白色填充
        painter.end()
