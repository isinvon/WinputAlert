
from winputalert.config.BaseConfig import BaseConfig


class ShakeAnimationConfig(BaseConfig):
    """ 抖动动画的配置类 """

    def __init__(self):
        # 调用父类构造函数，config_file 由 BaseConfig 默认值传入
        super().__init__()

    def get_animation_duration_time(self):
        """
        shake 抖动动画时长
        :return: int

        单位为毫秒(ms)

        默认值为 150
        """
        return self.config.getint("animation.shake", "animation_duration_time", fallback=150)

    def get_amplitude(self):
        """
        shake 抖动幅度
        :return: int

        单位为像素(px)

        默认值为 10
        """
        return self.config.getint("animation.shake", "amplitude", fallback=10)

    def set_animation_duration_time(self, value):
        """
        设置shake抖动动画时长

        :param value: int类型的值，表示动画时长（单位为毫秒）

        """
        self.config.set("animation.shake", "animation_duration_time", str(value))
        self.write_config()

    def set_amplitude(self, value):
        """
        设置shake抖动幅度

        :param value: int类型的值，表示抖动幅度（单位为像素）

        """
        self.config.set("animation.shake", "amplitude", str(value))
        self.write_config()