
from winputalert.config.BaseConfig import BaseConfig


class BaseAnimationConfig(BaseConfig):
    """ 
    基础动画配置
    
    方法：
        is_use_animation()
            是否使用动画
        get_animation_type()
            动画类型
    """
    def __init__(self):
        # 调用父类构造函数，config_file 由 BaseConfig 默认值传入
        super().__init__()
    
    def get_is_use_animation(self):
        """ 
        是否使用动画
        :return: bool
        
        """
        return self.config.getboolean("animation", "is_use_animation",fallback=None)


    def get_animation_type(self):
        """
        动画类型
        :return: str

        默认值为 fade_in - 淡入动画
        """
        return self.config.get("animation", "animation_type",fallback="fade_in")
    
    def set_is_use_animation(self, value):
        """
        设置是否使用动画

        :param value: bool类型的值，表示是否使用动画

        """
        self.config.set("animation", "is_use_animation", str(value))
        self.write_config()

    def set_animation_type(self, value):
        """
        设置动画类型

        :param value: str类型的值，表示动画类型

        """
        self.config.set("animation", "animation_type", value)
        self.write_config()
    