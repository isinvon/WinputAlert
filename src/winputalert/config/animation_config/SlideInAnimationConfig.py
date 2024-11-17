
from winputalert.config.BaseConfig import BaseConfig


class SlideInAnimationConfig(BaseConfig):
    """ 滑入动画的配置类 """

    def __init__(self):
        # 调用父类构造函数，config_file 由 BaseConfig 默认值传入
        super().__init__()

    def get_animation_duration_time(self):
        """
        slide_in 滑入动画时长
        :return: int

        单位为毫秒(ms)

        默认值为 150
        """
        return self.config.getint("animation.slide_in", "animation_duration_time", fallback=150)

    def get_direction(self):
        """
        slide_in 滑入方向
        :return: str

        可选值："left", "right", "up", "down"

        默认值为 "up"
        """
        return self.config.get("animation.slide_in", "direction", fallback="up")

    def get_amplitude(self):
        """
        slide_in 滑入幅度
        :return: int

        单位为像素(px)

        默认值为 1
        """
        return self.config.getint("animation.slide_in", "amplitude", fallback=1)

    def set_animation_duration_time(self, value):
        """
        设置slide_in滑入动画时长

        :param value: int类型的值，表示动画时长（单位为毫秒）

        """
        self.config.set("animation.slide_in", "animation_duration_time", str(value))
        self.write_config()

    def set_direction(self, value):
        """
        设置slide_in滑入方向

        :param value: str类型的值，表示滑入方向（可选值："left", "right", "up", "down"）

        """
        self.config.set("animation.slide_in", "direction", value)
        self.write_config()

    def set_amplitude(self, value):
        """
        设置slide_in滑入幅度

        :param value: int类型的值，表示滑入幅度（单位为像素）

        """
        self.config.set("animation.slide_in", "amplitude", str(value))
        self.write_config()