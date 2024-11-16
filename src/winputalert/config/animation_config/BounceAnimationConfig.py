
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
