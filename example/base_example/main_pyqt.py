# pip install PyQt5_stubs, 而不是pip install PyQt 参考：https://blog.csdn.net/qq527703883/article/details/116536345
from PyQt5.QtWidgets import QApplication, QWidget, QLabel  # type: ignore
from PyQt5.QtCore import Qt, QRectF  # type: ignore
from PyQt5.QtGui import QColor, QPainter, QPainterPath, QRegion, QFont  # type: ignore
import sys


class TransparentWindow(QWidget):
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
        
        # 设置窗口置顶（这行代码不允许出现在self.setWindowFlags(Qt.Tool)之前，否则置顶效果不起作用）
        # 原因是：
        # 1. self.setWindowFlags(Qt.Tool) 这行代码。Qt.Tool 标志通常用于工具窗口，这种窗口通常不会显示在任务栏中，并且可能不会像普通窗口那样响应某些窗口管理操作。
        # 2. 当您设置 Qt.Tool 标志时，它可能会覆盖或影响 Qt.WindowStaysOnTopHint 标志的效果。这可能是导致窗口置顶不起作用的原因。
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)


        # 设置标签和字体
        label = QLabel('中', self)
        # font = QFont('Arial', 40)  # 设置字体和大小
        # font.setWeight(10000)  # 设置字体为超级粗体
        # label.setFont(font)
        label.setStyleSheet("font: 40pt '黑体'; font-weight: bold;")  # 设置字体为粗体
        label.setAlignment(Qt.AlignCenter)  # 设置文字居中
        label.setGeometry(0, 0, window_width, window_height)

        # 显示窗口
        self.show()

    def paintEvent(self, event):
        """ 
        重写paintEvent方法，实现窗口的圆角效果

        Args:
            event (QPaintEvent): 绘制事件对象

        Returns:
            None

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TransparentWindow()
    sys.exit(app.exec_())
