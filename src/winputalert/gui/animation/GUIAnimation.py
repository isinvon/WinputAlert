# from PyQt5.QtCore import QEasingCurve, QPoint, QPropertyAnimation, QRectF
# from PyQt5.QtGui import QColor
# from PyQt5.QtWidgets import QWidget


# class GUIAnimation(QWidget):
#     """提供多个窗口动画效果的类"""
    
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.animation = None

#     def start_fade_in_animation(self, duration=150, start_opacity=0, end_opacity=1):
#         """渐显动画：窗口逐渐从透明变为不透明"""
#         self.animation = QPropertyAnimation(self, b"windowOpacity")
#         self.animation.setDuration(duration)
#         self.animation.setStartValue(start_opacity)
#         self.animation.setEndValue(end_opacity)
#         self.animation.start()

#     def start_bounce_animation(self, duration=500, start_pos=QPoint(0, 0),
#                                mid_pos=QPoint(100, 100), end_pos=QPoint(10, 10)):
#         """弹跳动画：模拟窗口从起始点弹跳到目标点"""
#         self.animation = QPropertyAnimation(self, b"pos")
#         self.animation.setDuration(duration)
#         self.animation.setStartValue(start_pos)
#         self.animation.setKeyValueAt(0.5, mid_pos)  # 中间位置
#         self.animation.setEndValue(end_pos)
#         self.animation.setEasingCurve(QEasingCurve.OutBounce)
#         self.animation.start()

#     def start_shake_animation(self, duration=150, amplitude=10):
#         """抖动动画：窗口快速左右抖动"""
#         self.animation = QPropertyAnimation(self, b"pos")
#         self.animation.setDuration(duration)
#         self.animation.setStartValue(self.pos())
#         self.animation.setKeyValueAt(
#             0.1, QPoint(self.x() + amplitude, self.y()))
#         self.animation.setKeyValueAt(
#             0.2, QPoint(self.x() - amplitude, self.y()))
#         self.animation.setKeyValueAt(
#             0.3, QPoint(self.x() + amplitude, self.y()))
#         self.animation.setKeyValueAt(
#             0.4, QPoint(self.x() - amplitude, self.y()))
#         self.animation.setKeyValueAt(0.5, self.pos())
#         self.animation.setEndValue(self.pos())
#         self.animation.setEasingCurve(QEasingCurve.Linear)
#         self.animation.start()

#     def start_slide_in_animation(self, direction="up", duration=150, distance=None, amplitude=1):
#         """滑入动画：窗口从屏幕外滑入当前屏幕"""
#         if direction == "left":
#             start_pos = QPoint(
#                 self.x() - (distance or self.width()) * amplitude, self.y())
#         elif direction == "right":
#             start_pos = QPoint(
#                 self.x() + (distance or self.width()) * amplitude, self.y())
#         elif direction == "up":
#             start_pos = QPoint(self.x(), self.y() -
#                                (distance or self.height()) * amplitude)
#         elif direction == "down":
#             start_pos = QPoint(self.x(), self.y() +
#                                (distance or self.height()) * amplitude)

#         self.animation = QPropertyAnimation(self, b"pos")
#         self.animation.setDuration(duration)
#         self.animation.setStartValue(start_pos)
#         self.animation.setEndValue(self.pos())
#         self.animation.setEasingCurve(QEasingCurve.OutCubic)
#         self.animation.start()

#     def start_scale_up_animation(self, duration=150, start_rect=None):
#         """缩放动画：窗口从小逐渐放大到正常大小"""
#         if not start_rect:
#             start_rect = QRectF(self.x() + 100, self.y() + 100, 0, 0)
#         self.animation = QPropertyAnimation(self, b"geometry")
#         self.animation.setDuration(duration)
#         end_rect = self.geometry()
#         self.animation.setStartValue(start_rect)
#         self.animation.setEndValue(end_rect)
#         self.animation.setEasingCurve(QEasingCurve.OutQuad)
#         self.animation.start()
