from PySide6.QtCore import QEasingCurve, QPoint, QPropertyAnimation, QRectF, Qt
from PySide6.QtGui import QColor, QPainter, QPainterPath, QRegion
from PySide6.QtWidgets import QApplication, QLabel, QWidget

from winputalert.config.animation_config.BaseAnimationConfig import \
    BaseAnimationConfig
from winputalert.config.animation_config.BounceAnimationConfig import \
    BounceAnimationConfig
from winputalert.config.animation_config.FadeInAnimationConfig import \
    FadeInAnimationConfig
from winputalert.config.animation_config.ScaleUpAnimationConfig import \
    ScaleUpAnimationConfig
from winputalert.config.animation_config.ShakeAnimationConfig import \
    ShakeAnimationConfig
from winputalert.config.animation_config.SlideInAnimationConfig import \
    SlideInAnimationConfig
from winputalert.config.GuiConfig import GUIConfig


class TransparentWindow(QWidget):
    """ 透明窗口 """

    global gui_config

    gui_config = GUIConfig()

    def __init__(self, text, color=QColor(gui_config.get_bg_color_r(),  gui_config.get_bg_color_g(), gui_config.get_bg_color_b()), opacity=gui_config.get_gui_opacity()):

        super().__init__()

        gui_config = GUIConfig()

        self.setWindowOpacity(opacity)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint |  # 增加窗口无边框功能
                            Qt.WindowType.Tool | Qt.WindowType.WindowStaysOnTopHint |  # 增加窗口置顶
                            Qt.WindowType.WindowTransparentForInput)  # 增加透明穿透功能(让鼠标无法点击GUI，直接穿透到背部应用)

        self.window_width, self.window_height = gui_config.get_gui_width(
        ), gui_config.get_gui_height()

        self.screen = QApplication.primaryScreen().geometry()

        # TODO 是否要考虑到任务栏高度和不同屏幕分辨率（需要考虑使用 DPI 来计算宽度和高度）
        # 调用设置位置的函数
        self.set_position(gui_config.get_gui_pos())

        # 嵌入字体
        label = QLabel(text, self)
        # 字体颜色
        font_color = QColor(gui_config.get_gui_font_color_r(
        ), gui_config.get_gui_font_color_g(), gui_config.get_gui_font_color_b())
        label.setStyleSheet(
            f"font: {gui_config.get_gui_font_size()}pt '{gui_config.get_gui_font()}'; "
            f"font-weight: bold; color: rgb({font_color.red()}, {font_color.green()}, {font_color.blue()});"
        )
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setGeometry(0, 0, self.window_width, self.window_height)

        self.color = color
        self.show()

        base_animation_config = BaseAnimationConfig()

        # 设置动画过渡
        if base_animation_config.is_use_animation():
            if base_animation_config.get_animation_type() == "fade_in":
                # 获取配置
                fade_in_config = FadeInAnimationConfig()
                duration = fade_in_config.get_animation_duration_time()
                start_opacity = fade_in_config.get_start_opacity()
                end_opacity = fade_in_config.get_end_opacity()
                #  淡入动画
                self.start_fade_in_animation(
                    duration=duration, start_opacity=start_opacity, end_opacity=end_opacity)

            elif base_animation_config.get_animation_type() == "bounce":
                # 获取配置
                bounce_config = BounceAnimationConfig()
                duration = bounce_config.get_animation_duration_time()
                start_pos_x = bounce_config.get_start_pos_x()
                start_pos_y = bounce_config.get_start_pos_y()
                mid_pos_x = bounce_config.get_mid_pos_x()
                mid_pos_y = bounce_config.get_mid_pos_y()
                end_pos_x = bounce_config.get_end_pos_x()
                end_pos_y = bounce_config.get_end_pos_y()
                #  弹性动画
                self.start_bounce_animation(duration=duration, start_pos=QPoint(
                    start_pos_x, start_pos_y), mid_pos=QPoint(mid_pos_x, mid_pos_y), end_pos=QPoint(end_pos_x, end_pos_y))

            elif base_animation_config.get_animation_type() == "shake":
                # 获取配置
                shake_config = ShakeAnimationConfig()
                duration = shake_config.get_animation_duration_time()
                amplitude = shake_config.get_amplitude()
                # 抖动
                self.start_shake_animation(
                    duration=duration, amplitude=amplitude)

            elif base_animation_config.get_animation_type() == "slide_in":
                # 获取配置
                slide_in_config = SlideInAnimationConfig()
                duration = slide_in_config.get_animation_duration_time()
                direction = slide_in_config.get_direction()
                amplitude = slide_in_config.get_amplitude()
                # 缩小
                self.start_slide_in_animation(
                    duration=duration, direction=direction, amplitude=amplitude)

            elif base_animation_config.get_animation_type() == "scale_up":
                # 获取配置
                scale_up_config = ScaleUpAnimationConfig()
                duration = scale_up_config.get_animation_duration_time()
                # 放大
                self.start_scale_up_animation(duration=duration)
            else:
                # 默认使用淡入动画
                self.start_fade_in_animation()
        else:
            pass

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(self.color)
        painter.setPen(Qt.PenStyle.NoPen)

        radius = gui_config.get_gui_border_radius()
        rectf = QRectF(self.rect())
        path = QPainterPath()
        path.addRoundedRect(rectf, radius, radius)

        region = QRegion(path.toFillPolygon().toPolygon())
        self.setMask(region)

        painter.fillPath(path, QColor(self.color.red(),
                         self.color.green(), self.color.blue(), 100))
        painter.end()

    def set_position(self, position):
        """根据配置设置窗口位置"""
        margin_x = self.screen.width() // 100
        margin_y = self.screen.height() // 100

        if position == "left_top":
            x, y = margin_x, margin_y
        elif position == "top_center":
            x, y = (self.screen.width() - self.window_width) // 2, margin_y
        elif position == "right_top":
            x, y = self.screen.width() - self.window_width - margin_x, margin_y
        elif position == "left_center":
            x, y = margin_x, (self.screen.height() - self.window_height) // 2
        elif position == "center":
            x, y = (self.screen.width(
            ) - self.window_width) // 2, (self.screen.height() - self.window_height) // 2
        elif position == "right_center":
            x, y = self.screen.width() - self.window_width - \
                margin_x, (self.screen.height() - self.window_height) // 2
        elif position == "left_bottom":
            x, y = margin_x, self.screen.height() - self.window_height - margin_y
        elif position == "bottom_center":
            x, y = (self.screen.width(
            ) - self.window_width) // 2, self.screen.height() - self.window_height - margin_y
        elif position == "right_bottom":
            x, y = self.screen.width() - self.window_width - \
                margin_x, self.screen.height() - self.window_height - margin_y
        else:
            x, y = 0, 0  # 默认位置

        self.setGeometry(x, y, self.window_width, self.window_height)

    # ===========GUI动画选型======================================================
    # *测试通过

    def start_fade_in_animation(self, duration=150, start_opacity=0, end_opacity=1):
        """Starts a fade-in animation to smoothly show the window."""
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(duration)  # Duration in milliseconds
        self.animation.setStartValue(start_opacity)
        self.animation.setEndValue(end_opacity)
        self.animation.start()

    # *测试通过

    def start_bounce_animation(self, duration=500, start_pos=QPoint(0, 0), mid_pos=QPoint(100, 100), end_pos=QPoint(10, 10)):
        """弹性/回弹效果动画，模拟窗口弹跳移动"""
        self.animation = QPropertyAnimation(self, b"pos")
        self.animation.setDuration(duration)  # 动画持续时间
        self.animation.setStartValue(start_pos)  # 起始位置
        # self.animation.setKeyValueAt(0.2, mid_pos)  # 中间位置
        # 可继续添加...
        self.animation.setKeyValueAt(0.5, mid_pos)  # 中间位置
        self.animation.setEndValue(end_pos)  # 目标位置
        self.animation.setEasingCurve(QEasingCurve.OutBounce)
        self.animation.start()

    # *测试通过
    def start_shake_animation(self, duration=150, amplitude=10):
        """窗口抖动效果"""
        self.animation = QPropertyAnimation(self, b"pos")
        self.animation.setDuration(duration)
        self.animation.setStartValue(self.pos())
        # 设置多次位置偏移来模拟抖动效果
        self.animation.setKeyValueAt(0.1, QPoint(
            self.x() + amplitude, self.y()))
        self.animation.setKeyValueAt(0.2, QPoint(
            self.x() - amplitude, self.y()))
        self.animation.setKeyValueAt(0.3, QPoint(
            self.x() + amplitude, self.y()))
        self.animation.setKeyValueAt(0.4, QPoint(
            self.x() - amplitude, self.y()))
        self.animation.setKeyValueAt(0.5, self.pos())  # 最后回到原位置
        self.animation.setEndValue(self.pos())  # 最终回到原位置(添加结束值)
        self.animation.setEasingCurve(QEasingCurve.Linear)
        self.animation.start()

    # *测试通过
    def start_slide_in_animation(self, direction="up", duration=150, distance=None, amplitude=1):
        """滑入动画

        Args:
            direction (str): 滑入方向 ("left", "right", "up", "down")
            duration (int): 动画持续时间（毫秒）
            distance (int, optional): 滑入距离，若不设置则根据窗口宽高计算
            amplitude (float): 幅度因子，用于调整滑入距离，默认为1


        Parameters:

            ========= ========== ================================
            参数       含义             优先级
            ========= ========== ================================
            distance   指定滑入距离   优先级最高
            amplitude  调整倍数       次优先
            默认宽高    默认计算距离   最低优先级
            ========= ========== ================================


            在滑入动画中，distance 是一个可选参数，用来明确指定窗口滑入的距离。具体来说：

            如果设置了 distance：窗口会从当前位置向外移动指定的像素距离，作为动画的起始位置。
            如果未设置 distance：系统会根据窗口的宽度或高度（视方向而定）计算默认滑入距离。


        示例:

            self.start_slide_in_animation(direction="left", distance=200)
            - 设置了 distance=200，滑入距离固定为 200 像素。
            - amplitude 未设置或无效。
            窗口起始位置为 (-100, 100)，最终位置为 (100, 100)。

            self.start_slide_in_animation(direction="up", distance=150, amplitude=2)
            - 设置了 distance=150，滑入距离固定为 150 像素。
            - amplitude=2 对 distance 无效。
            窗口起始位置为 (100, -50)，最终位置为 (100, 100)。

        """
        if direction == "left":
            start_pos = QPoint(
                self.x() - (distance or self.width()) * amplitude, self.y())
        elif direction == "right":
            start_pos = QPoint(
                self.x() + (distance or self.width()) * amplitude, self.y())
        elif direction == "up":
            start_pos = QPoint(self.x(), self.y() -
                               (distance or self.height()) * amplitude)
        elif direction == "down":
            start_pos = QPoint(self.x(), self.y() +
                               (distance or self.height()) * amplitude)

        self.animation = QPropertyAnimation(self, b"pos")
        self.animation.setDuration(duration)
        # 从起始位置开始动画
        self.animation.setStartValue(start_pos)
        # 最终位置为窗口的当前位置
        self.animation.setEndValue(self.pos())
        self.animation.setEasingCurve(QEasingCurve.OutCubic)
        self.animation.start()

    # *测试通过
    def start_scale_up_animation(self, duration=150, start_rect=None):
        """缩放动画，窗口从小到大

        Args:
            duration (int, optional): 动画持续时间，单位为毫秒。默认值为 150。
            start_rect (QRectF, optional): 动画起始矩形，指定起始位置和大小。默认值为 None。

        参数示例:
            - duration = 200
            - start_rect = QRectF(self.x() + 100, self.y() + 100, 0, 0)

        注意:
            - `start_rect` 参数指定动画开始时的矩形位置和大小。`QRectF(x, y, width, height)` 中：
                - `x` 和 `y` 是矩形的左上角坐标，表示动画起始位置。
                - `width` 和 `height` 是矩形的宽度和高度，通常设置为 `0`，表示动画从一个小的矩形开始，逐步扩大到窗口的原始大小。

            - 例如，`QRectF(self.x() + 100, self.y() + 100, 0, 0)` 表示动画从窗口位置 `(self.x() + 100, self.y() + 100)` 开始，且宽度和高度为 `0`，即动画开始时窗口不可见，随后逐渐放大到窗口的真实尺寸。

            - `end_rect` 是窗口的最终几何形状，通常通过 `self.geometry()` 获取，即窗口的当前矩形（包括位置和尺寸）。

            - 如果你希望窗口从一个更具位置感知的起始点（例如从中心或角落）开始放大，你可以调整 `start_rect` 的位置，确保动画效果符合你的需求。

            - `QRectF` 构造函数中的参数含义：
                - `x`：矩形的左上角的水平坐标。
                - `y`：矩形的左上角的垂直坐标。
                - `width`：矩形的宽度。
                - `height`：矩形的高度。

        """
        if not start_rect:
            start_rect = QRectF(self.x() + 100,
                                self.y() + 100, 0, 0)
        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(duration)
        end_rect = self.geometry()
        self.animation.setStartValue(start_rect)
        self.animation.setEndValue(end_rect)
        self.animation.setEasingCurve(QEasingCurve.OutQuad)
        self.animation.start()

    # !!测试不通过
    # def start_change_color_animation(self, start_color=QColor(255, 0, 0), end_color=QColor(0, 255, 0), duration=150):
    #     """改变背景颜色动画"""
    #     color_animation = QPropertyAnimation(self, b"color")
    #     color_animation.setDuration(duration)
    #     color_animation.setStartValue(start_color)
    #     color_animation.setEndValue(end_color)
    #     color_animation.start()
