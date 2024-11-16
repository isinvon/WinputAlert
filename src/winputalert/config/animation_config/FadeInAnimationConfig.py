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