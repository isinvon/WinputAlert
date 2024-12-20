from winputalert.config.BaseConfig import BaseConfig


class ScaleUpAnimationConfig(BaseConfig):
    """ 放大动画的配置类 """

    def __init__(self):
        # 调用父类构造函数，config_file 由 BaseConfig 默认值传入
        super().__init__()

    def get_animation_duration_time(self):
        """
        获取scale_up放大动画时长

        单位为毫秒(ms)，默认值为 150
        """
        return self.config.getint("animation.scale_up",
                                  "animation_duration_time",
                                  fallback=150)

    def set_animation_duration_time(self, value, intensity="weak"):
        """
        设置scale_up放大动画时长
        """
        self.config.set("animation.scale_up",
                        "animation_duration_time", 
                        str(value))
        self.write_config()