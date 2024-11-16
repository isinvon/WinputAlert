
# from winputalert.config.BaseConfig import BaseConfig

# class ChangeColorAnimationConfig(BaseConfig):
#     """ 颜色变化动画的配置类 """

#     def __init__(self):
#         # 调用父类构造函数，config_file 由 BaseConfig 默认值传入
#         super().__init__()

#     def change_color_animation_duration(self):
#         """
#         change_color 颜色变化动画时长
#         :return: int

#         单位为毫秒(ms)

#         默认值为 150
#         """
#         return self.config.getint("animation.change_color", "animation_duration_time", fallback=150)