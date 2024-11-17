from winputalert.config.BaseConfig import BaseConfig


class KeyboardConfig(BaseConfig):
    """ 对键盘的配置类 """

    def __init__(self):
        # 调用父类构造函数，config_file 由 BaseConfig 默认值传入
        super().__init__()

    def get_keyboard_detect_time_interval(self):
        """ 
        获取键盘检测时间
        """
        return self.config.getint('keyboard', 'keyboard_detect_time_interval', fallback=None)

    def set_keyboard_detect_time_interval(self, value):
        """
        设置键盘检测时间

        :param value: 要设置的键盘检测时间值
        """
        self.config.set('keyboard', 'keyboard_detect_time_interval', str(value))
        self.write_config()