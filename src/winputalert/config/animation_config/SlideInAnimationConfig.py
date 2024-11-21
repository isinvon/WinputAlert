from winputalert.config.BaseConfig import BaseConfig


class SlideInAnimationConfig(BaseConfig):
    """ 滑入动画的配置类 """

    def __init__(self):
        # 调用父类构造函数，config_file 由 BaseConfig 默认值传入
        super().__init__()

    def get_animation_duration_time(self, direction="up"):
        """
        获取slide_in滑入动画时长

        :param direction: str类型，表示滑入方向，取值为 "left", "right", "up", "down"
        :return: int

        单位为毫秒(ms)，默认值为 150
        """
        section = f"animation.slide_in.{direction}"
        return self.config.getint(section, "animation_duration_time", fallback=150)

    def get_direction(self, direction="up"):
        """
        获取slide_in滑入方向

        :param direction: str类型，表示滑入方向，取值为 "left", "right", "up", "down"
        :return: str

        默认值为 "up"
        """
        section = f"animation.slide_in.{direction}"
        return self.config.get(section, "direction", fallback="up")

    def get_amplitude(self, direction="up"):
        """
        获取slide_in滑入幅度

        :param direction: str类型，表示滑入方向，取值为 "left", "right", "up", "down"
        :return: int

        单位为像素(px)，默认值为 1
        """
        section = f"animation.slide_in.{direction}"
        return self.config.getint(section, "amplitude", fallback=1)

    def set_animation_duration_time(self, value, direction="up"):
        """
        设置slide_in滑入动画时长

        :param value: int类型的值，表示动画时长（单位为毫秒）
        :param direction: str类型，表示滑入方向，取值为 "left", "right", "up", "down"
        """
        section = f"animation.slide_in.{direction}"
        self.config.set(section, "animation_duration_time", str(value))
        self.write_config()

    def set_direction(self, value, direction="up"):
        """
        设置slide_in滑入方向

        :param value: str类型的值，表示滑入方向（可选值："left", "right", "up", "down"）
        :param direction: str类型，表示滑入方向，取值为 "left", "right", "up", "down"
        """
        section = f"animation.slide_in.{direction}"
        self.config.set(section, "direction", value)
        self.write_config()

    def set_amplitude(self, value, direction="up"):
        """
        设置slide_in滑入幅度

        :param value: int类型的值，表示滑入幅度（单位为像素）
        :param direction: str类型，表示滑入方向，取值为 "left", "right", "up", "down"
        """
        section = f"animation.slide_in.{direction}"
        self.config.set(section, "amplitude", str(value))
        self.write_config()
