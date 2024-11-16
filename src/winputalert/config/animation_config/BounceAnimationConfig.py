
from winputalert.config.BaseConfig import BaseConfig


class BounceAnimationConfig(BaseConfig):
    """ 弹跳动画的配置类 """

    def __init__(self):
        # 调用父类构造函数，config_file 由 BaseConfig 默认值传入
        super().__init__()

    def get_animation_duration_time(self):
        """
        bounce 弹跳动画时长
        :return: int

        单位为毫秒(ms)

        默认值为 150
        """
        return self.config.getint("animation.bounce", "animation_duration_time", fallback=150)

    def get_start_pos_x(self):
        """
        bounce 弹跳动画起始位置 x 坐标
        :return: int

        单位为像素(px)

        默认值为 0
        """
        return self.config.getint("animation.bounce", "start_pos_x", fallback=0)

    def get_start_pos_y(self):
        """
        bounce 弹跳动画起始位置 y
        :return: int

        单位为像素(px)

        默认值为 0
        """
        return self.config.getint("animation.bounce", "start_pos_y", fallback=0)

    def get_mid_pos_x(self):
        """
        bounce 弹跳动画中间位置 x
        :return: int

        单位为像素(px)

        默认值为 75
        """
        return self.config.getint("animation.bounce", "mid_pos_x", fallback=75)

    def get_mid_pos_y(self):
        """
        bounce 弹跳动画中间位置 y

        :return: int

        单位为像素(px)

        默认值为 50
        """
        return self.config.getint("animation.bounce", "mid_pos_y", fallback=50)

    def get_end_pos_x(self):
        """
        bounce 弹跳动画结束位置 x
        :return: int

        单位为像素(px)

        默认值为 50
        """
        return self.config.getint("animation.bounce", "end_pos_x", fallback=50)

    def get_end_pos_y(self):
        """
        bounce 弹跳动画结束位置 y
        :return: int

        单位为像素(px)

        默认值为 50
        """
        return self.config.getint("animation.bounce", "end_pos_y", fallback=50)

    def set_animation_duration_time(self, value):
        """
        设置bounce弹跳动画时长

        :param value: int类型的值，表示动画时长（单位为毫秒）

        """
        self.config.set("animation.bounce", "animation_duration_time", str(value))
        self.write_config()

    def set_start_pos_x(self, value):
        """
        设置bounce弹跳动画起始位置x坐标

        :param value: int类型的值，表示x坐标（单位为像素）

        """
        self.config.set("ananimation.bounce", "start_pos_x", str(value))
        self.write_config()

    def set_start_pos_y(self, value):
        """
        设置bounce弹跳动画起始位置y坐标

        :param value: int类型的值，表示y坐标（单位为像素）

        """
        self.config.set("animation.bounce", "start_pos_y", str(value))
        self.write_config()

    def set_mid_pos_x(self, value):
        """
        设置bounce弹跳动画中间位置x坐标

        :param value: int类型的值，表示x坐标（单位为像素）

        """
        self.config.set("animation.bounce", "mid_pos_x", str(value))
        self.write_config()

    def set_mid_pos_y(self,
                    value):
        """
        设置bounce弹跳动画中间位置y坐标

        :param value: int类型的值，表示y坐标（单位为像素）

        """
        self.config.set("animation.bounce", "mid_pos_y", str(value))
        self.write_config()

    def set_end_pos_x(self, value):
        """
        设置bounce弹跳动画结束位置x坐标

        :param value: int类型的值，表示x坐标（单位为像素）

        """
        self.config.set("animation.bounce", "end_pos_x", str(value))
        self.write_config()

    def set_end_pos_y(self, value):
        """
        设置bounce弹跳动画结束位置y坐标

        :param value: int类型的值，表示y坐标（单位为像素）

        """
        self.config.set("animation.bounce", "end_pos_y", str(value))
        self.write_config()