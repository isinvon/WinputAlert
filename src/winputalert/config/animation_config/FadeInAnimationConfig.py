from winputalert.config.BaseConfig import BaseConfig


class FadeInAnimationConfig(BaseConfig):
    """ 淡入动画的配置类 """

    def __init__(self):
        # 调用父类构造函数，config_file 由 BaseConfig 默认值传入
        super().__init__()

    def get_animation_duration_time(self):
        """
        fade_in 淡入动画时长
        :return: int

        单位为毫秒(ms)

        默认值为 150
        """
        return self.config.getint("animation.fade_in", "animation_duration_time", fallback=150)

    def get_start_opacity(self):
        """
        淡入动画开始时的透明度
        :return: float

        取值范围为 0.0 ~ 1.0

        默认值为 0.0
        """
        return self.config.getfloat("animation.fade_in", "start_opacity", fallback=0.0)

    def get_end_opacity(self):
        """
        淡入动画结束时的透明度
        :return: float
        
        取值范围为 0.0 ~ 1.0
        
        默认值为 1.0
        """
        return self.config.getfloat("animation.fade_in", "end_opacity", fallback=1.0)
    
    def set_animation_duration_time(self, value):
        """
        设置fade_in淡入动画时长

        :param value: int类型的值，表示动画时长（单位为毫秒）

        """
        self.config.set("animation.fade_in", "animation_duration_time", str(value))
        self.write_config()

    def set_start_opacity(self, value):
        """
        设置淡入动画开始时的透明度

        :param value: float类型的值，表示透明度（取值范围为0.0 ~ 1.0）

        """
        self.config.set("animation.fade_in", "start_opacity", str(value))
        self.write_config()

    def set_end_opacity(self, value):
        """
        设置淡入动画结束时的透明度

        :param value: float类型的值，表示透明度（取值范围为0.0 ~ 1.0）

        """
        self.config.set("animation.fade_in", "end_opacity", str(value))
        self.write_config()