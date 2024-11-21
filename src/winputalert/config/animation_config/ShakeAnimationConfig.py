from winputalert.config.BaseConfig import BaseConfig


class ShakeAnimationConfig(BaseConfig):
    """ 抖动动画的配置类 """

    def __init__(self):
        # 调用父类构造函数，config_file 由 BaseConfig 默认值传入
        super().__init__()

    def get_animation_duration_time(self, intensity="weak"):
        """
        获取shake抖动动画时长

        :param intensity: str类型，表示抖动强度，取值为 "weak"、"medium" 或 "strong"
        :return: int

        单位为毫秒(ms)，默认值为 150
        """
        section = f"animation.shake.{intensity}"
        return self.config.getint(section, "animation_duration_time", fallback=150)

    def get_amplitude(self, intensity="weak"):
        """
        获取shake抖动幅度

        :param intensity: str类型，表示抖动强度，取值为 "weak"、"medium" 或 "strong"
        :return: int

        单位为像素(px)，默认值为 10
        """
        section = f"animation.shake.{intensity}"
        return self.config.getint(section, "amplitude", fallback=10)

    def set_animation_duration_time(self, value, intensity="weak"):
        """
        设置shake抖动动画时长

        :param value: int类型，表示动画时长（单位为毫秒）
        :param intensity: str类型，表示抖动强度，取值为 "weak"、"medium" 或 "strong"
        """
        section = f"animation.shake.{intensity}"
        self.config.set(section, "animation_duration_time", str(value))
        self.write_config()

    def set_amplitude(self, value, intensity="weak"):
        """
        设置shake抖动幅度

        :param value: int类型，表示抖动幅度（单位为像素）
        :param intensity: str类型，表示抖动强度，取值为 "weak"、"medium" 或 "strong"
        """
        section = f"animation.shake.{intensity}"
        self.config.set(section, "amplitude", str(value))
        self.write_config()
