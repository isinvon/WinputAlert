import configparser
import os
from platformdirs import user_data_dir


class BaseConfig:
    """
    基础配置类，用于读取配置文件
    """
    # def get_config_path():
    #     """
    #     获取配置文件路径

    #     see: https://blog.csdn.net/a772304419/article/details/139993938
    #     """
    #     return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
    @staticmethod
    def get_config_path():
        r""" 
        获取配置文件路径
        这个方法会返回用户特定的配置文件路径，即 
        C:\Users\<username>\AppData\Roaming\WinputAlert\config.ini
        如果该路径下没有配置文件，则回退到当前脚本同级目录下的config.ini。
        """
        app_name = "WinputAlert"
        app_author = os.getlogin()  # 获取当前登录的用户名

        # 获取用户数据目录路径
        user_data_dir_path = user_data_dir(
            appname=app_name, appauthor=app_author)

        # 用户数据目录下的配置文件路径
        config_path = os.path.join(user_data_dir_path, "config.ini")

        # 如果用户数据目录下的配置文件不存在，则使用当前脚本同级目录下的config.ini
        if not os.path.isfile(config_path):
            config_path = os.path.join(os.path.dirname(
                os.path.abspath(__file__)), "config.ini")

        return config_path

    def __init__(self, config_file=None):
        """ 
        如果传入的config_file为None，则使用默认的get_config_path方法获取配置文件路径
        """
        if config_file is None:
            config_file = self.get_config_path()

        self.config = configparser.ConfigParser()
        self.config_file = config_file  # 配置文件路径
        self.read_config()

    def read_config(self):
        """读取配置文件，指定编码"""
        try:
            with open(self.config_file, encoding='utf-8') as file:
                self.config.read_file(file)
        except FileNotFoundError:
            print(f"配置文件 {self.config_file} 未找到")
        except Exception as e:
            print(f"读取配置文件时发生错误: {e}")

    def write_config(self):
        """
        将当前配置写入配置文件，指定编码
        """
        try:
            with open(self.config_file, 'w', encoding='utf-8') as file:
                self.config.write(file)
        except Exception as e:
            print(f"写入配置文件时发生错误: {e}")

    def set_option(self, section, option, value):
        """
        设置指定节（section）下的选项（option）的值，并更新配置文件

        :param section: 配置文件中的节名，如 [gui]、[keyboard]等
        :param option: 节内的具体选项名，如width、font_size等
        :param value: 要设置的新值
        """
        if not self.config.has_section(section):
            self.config.add_section(section)
        self.config.set(section, option, value)
        self.write_config()

    def batch_update_values(self, section, values):
        """
        批量更新指定节（section）下的多个选项（option）的值，并更新配置文件

        :param section: 配置文件中的节名，如 [gui]、[keyboard]等
        :param values: 一个字典，包含要更新的选项及其新值
        """
        if not self.config.has_section(section):
            self.config.add_section(section)

        for option, value in values.items():
            # 将所有值转换为字符串
            self.config.set(section, option, str(value))

        self.write_config()
