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
from winputalert.config.GUIConfig import GUIConfig


class TransparentWindow(QWidget):
    """ 透明窗口 """

    global gui_config

    gui_config = GUIConfig()

    def __init__(self, text):

        super().__init__()

        gui_config = GUIConfig()
        
        color=QColor(gui_config.get_bg_color_r(),  gui_config.get_bg_color_g(), gui_config.get_bg_color_b())
        
        opacity=gui_config.get_gui_opacity()

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

        if base_animation_config.get_is_use_animation():
            # 淡入
            if base_animation_config.get_animation_type() == "fade_in":
                fade_in_config = FadeInAnimationConfig()
                gui_config = GUIConfig()
                duration = fade_in_config.get_animation_duration_time()
                self.start_fade_in_animation(
                    duration=duration, end_opacity=gui_config.get_gui_opacity())
            # 弹性 (由位置改变出场方式)
            elif base_animation_config.get_animation_type() == "bounce":
                bounce_config = BounceAnimationConfig()
                gui_pos = GUIConfig().get_gui_pos()
                edge_offset = 25  # 距离屏幕边缘的偏移量
                self.start_bounce_animation(
                    direction=gui_pos,
                    duration=bounce_config.get_animation_duration_time(),
                    edge_offset=edge_offset
                )
            # 抖动（强）
            elif base_animation_config.get_animation_type() == "shake.strong":
                shake_config = ShakeAnimationConfig()
                duration = shake_config.get_animation_duration_time()
                amplitude = shake_config.get_amplitude(intensity="strong")
                self.start_shake_animation(
                    duration=duration, amplitude=amplitude)
            # 抖动 （中）
            elif base_animation_config.get_animation_type() == "shake.medium":
                shake_config = ShakeAnimationConfig()
                duration = shake_config.get_animation_duration_time()
                amplitude = shake_config.get_amplitude(intensity="medium")
                self.start_shake_animation(
                    duration=duration, amplitude=amplitude)
            # 抖动（弱）
            elif base_animation_config.get_animation_type() == "shake.weak":
                shake_config = ShakeAnimationConfig()
                duration = shake_config.get_animation_duration_time()
                amplitude = shake_config.get_amplitude(intensity="weak")
                self.start_shake_animation(
                    duration=duration, amplitude=amplitude)
            # 放大
            elif base_animation_config.get_animation_type() == "scale_up":
                scale_up_config = ScaleUpAnimationConfig()
                duration = scale_up_config.get_animation_duration_time()
                self.start_scale_up_animation(
                    duration=duration)
            # 滑入(从上往下)
            elif base_animation_config.get_animation_type() == "slide_in.up":
                slide_in_config = SlideInAnimationConfig()
                duration = slide_in_config.get_animation_duration_time()
                direction = slide_in_config.get_direction(direction="up")
                amplitude = slide_in_config.get_amplitude()
                self.start_slide_in_animation(
                    duration=duration, direction=direction, amplitude=amplitude)
            # 滑入（从下往上）
            elif base_animation_config.get_animation_type() == "slide_in.down":
                slide_in_config = SlideInAnimationConfig()
                duration = slide_in_config.get_animation_duration_time()
                direction = slide_in_config.get_direction(direction="down")
                amplitude = slide_in_config.get_amplitude()
                self.start_slide_in_animation(
                    duration=duration, direction=direction, amplitude=amplitude)
            # 滑入（从左往右）
            elif base_animation_config.get_animation_type() == "slide_in.left":
                slide_in_config = SlideInAnimationConfig()
                duration = slide_in_config.get_animation_duration_time()
                direction = slide_in_config.get_direction(direction="left")
                amplitude = slide_in_config.get_amplitude()
                self.start_slide_in_animation(
                    duration=duration, direction=direction, amplitude=amplitude)
            # 滑入（从右往左）
            elif base_animation_config.get_animation_type() == "slide_in.right":
                slide_in_config = SlideInAnimationConfig()
                duration = slide_in_config.get_animation_duration_time()
                direction = slide_in_config.get_direction(direction="right")
                amplitude = slide_in_config.get_amplitude()
                self.start_slide_in_animation(
                    duration=duration, direction=direction, amplitude=amplitude)
            else:
                # 默认使用淡入动画
                self.start_fade_in_animation()

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
        # self.animation.setEasingCurve(QEasingCurve.InOutQuad)
        self.animation.start()

    # *测试通过
    def start_bounce_animation(self, direction="top_left", duration=150, mid_ratio=0.5, edge_offset=25):
        """
        弹性/回弹效果动画，支持从不同方向弹入
        :param direction: 弹入方向，可选值 "top_left", "top_center", "top_right", "left_center",
                        "right_center", "bottom_left", "bottom_center", "bottom_right"
        :param duration: 动画持续时间，单位毫秒
        :param mid_ratio: 中间位置的时间比例，默认 0.5 (动画时间的中点)
        """
        # 获取屏幕宽高
        screen_width = self.screen.width()
        screen_height = self.screen.height()

        # 获取窗口宽高
        config = GUIConfig()
        widget_width = config.get_gui_width()
        widget_height = config.get_gui_height()

        # 初始化坐标
        start_pos = QPoint()
        mid_pos = QPoint()
        end_pos = QPoint()

        # 偏移值，控制轨迹的相对弹入效果
        mid_offset_x = widget_width // 2  # 中间位置的水平偏移
        mid_offset_y = widget_height // 2  # 中间位置的垂直偏移
        edge_offset = 25  # 距离屏幕边缘的最终位置偏移

        # 根据方向动态计算位置
        if direction == "top_left":
            start_pos = QPoint(0, 0)
            mid_pos = QPoint(mid_offset_x, mid_offset_y)
            end_pos = QPoint(edge_offset, edge_offset)
        elif direction == "top_center":
            start_pos = QPoint((screen_width - widget_width) // 2, 0)
            mid_pos = QPoint((screen_width - widget_width) // 2, mid_offset_y)
            end_pos = QPoint((screen_width - widget_width) // 2, edge_offset)
        elif direction == "top_right":
            start_pos = QPoint(screen_width - widget_width, 0)
            mid_pos = QPoint(screen_width - widget_width - mid_offset_x, mid_offset_y)
            end_pos = QPoint(screen_width - widget_width - edge_offset, edge_offset)
        elif direction == "left_center":
            start_pos = QPoint(0, (screen_height - widget_height) // 2)
            mid_pos = QPoint(mid_offset_x, (screen_height - widget_height) // 2)
            end_pos = QPoint(edge_offset, (screen_height - widget_height) // 2)
        elif direction == "right_center":
            start_pos = QPoint(screen_width - widget_width, (screen_height - widget_height) // 2)
            mid_pos = QPoint(screen_width - widget_width - mid_offset_x, (screen_height - widget_height) // 2)
            end_pos = QPoint(screen_width - widget_width - edge_offset, (screen_height - widget_height) // 2)
        elif direction == "bottom_left":
            start_pos = QPoint(0, screen_height - widget_height)
            mid_pos = QPoint(mid_offset_x, screen_height - widget_height - mid_offset_y)
            end_pos = QPoint(edge_offset, screen_height - widget_height - edge_offset)
        elif direction == "bottom_center":
            start_pos = QPoint((screen_width - widget_width) // 2, screen_height - widget_height)
            mid_pos = QPoint((screen_width - widget_width) // 2, screen_height - widget_height - mid_offset_y)
            end_pos = QPoint((screen_width - widget_width) // 2, screen_height - widget_height - edge_offset)
        elif direction == "bottom_right":
            start_pos = QPoint(screen_width - widget_width, screen_height - widget_height)
            mid_pos = QPoint(screen_width - widget_width - mid_offset_x, screen_height - widget_height - mid_offset_y)
            end_pos = QPoint(screen_width - widget_width - edge_offset, screen_height - widget_height - edge_offset)
        else:
            raise ValueError(f"未知方向: {direction}")

        # 创建弹性动画
        self.animation = QPropertyAnimation(self, b"pos")
        self.animation.setDuration(duration)
        self.animation.setStartValue(start_pos)
        self.animation.setKeyValueAt(mid_ratio, mid_pos)
        self.animation.setEndValue(end_pos)
        
        # 使用更平滑的缓动函数，例如 InOutQuad
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)  # 可以根据需要选择更柔和的曲线
        self.animation.start()

    # *测试通过
    def start_shake_animation(self, duration=150, amplitude=10):
        """窗口抖动效果(丝滑版)"""
        current_pos = self.pos()  # 获取当前窗口位置

        # 创建动画
        self.animation = QPropertyAnimation(self, b"pos")
        self.animation.setDuration(duration)
        self.animation.setLoopCount(3)

        # 定义抖动路径
        self.animation.setKeyValueAt(0, current_pos)
        self.animation.setKeyValueAt(0.25, QPoint(
            current_pos.x() + amplitude, current_pos.y()))
        self.animation.setKeyValueAt(0.5, current_pos)
        self.animation.setKeyValueAt(0.75, QPoint(
            current_pos.x() - amplitude, current_pos.y()))
        self.animation.setKeyValueAt(1, current_pos)

        # 启动动画
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
