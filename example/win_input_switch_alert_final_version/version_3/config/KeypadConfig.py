from config.BaseConfig import BaseConfig


class KeypadConfig(BaseConfig):
    """ 对键盘的配置类 """
    def __init__(self):
        # 调用父类构造函数，config_file 由 BaseConfig 默认值传入
        super().__init__()

    def get_keypad_detect_time_interval(self):
        """ 
        获取键盘检测时间
        """
        return self.config.get('keypad', 'keypad_detect_time_interval', fallback=None)
