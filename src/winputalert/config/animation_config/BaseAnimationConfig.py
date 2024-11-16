
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
    
    def is_use_animation(self):
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
    
    
    