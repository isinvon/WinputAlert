from winputalert.config.BaseConfig import BaseConfig


class SystemConfig(BaseConfig):

    def __init__(self):
        # 调用父类构造函数，config_file 由 BaseConfig 默认值传入
        super().__init__()

    def get_auto_start_on_system_boot(self):
        """
        获取开机自启

        返回值:

            - 开机自启值
        返回值类型:

            - bool        
        默认值:

            - False：不开机自启
            - True：开机自启
        """
        return self.config.getboolean('system', 'auto_start_on_system_boot', fallback=True)

    def set_auto_start_on_system_boot(self, value):
        """
        设置开机自启

        类型:

            - bool

        参数:

            - value: 要设置的开机自启值

        可选值:

            - False：不开机自启
            - True：开机自启
        """
        self.config.set('system', 'auto_start_on_system_boot', str(value))
        self.write_config()
