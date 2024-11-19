import configparser
import os


class BaseConfig:
    """
    基础配置类，用于读取配置文件
    """
    def get_config_path():
        """ 
        获取配置文件路径

        see: https://blog.csdn.net/a772304419/article/details/139993938
        """
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')

    def __init__(self, config_file=get_config_path()):
        """ 
        千万不要用config.ini，因为会找不到，写config/config.ini就可以了,或者./config/config.ini
        """
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

        示例用法：
        
            # 创建BaseConfig实例
            config = BaseConfig()

            # 设置 [gui] 节下的width选项的值为150
            config.set_option('gui', 'width', '150')
        """
        if not self.config.has_section(section):
            self.config.add_section(section)
        self.config.set(section, option, value)
        self.write_config()

    def batch_update_values(self, section, values):
        """
        批量更新指定节（section）下的多个选项（option）的值，并更新配置文件(允许传入任何类型，最后都将转化为str然后写入ini文件)

        :param section: 配置文件中的节名，如 [gui]、[keyboard]等
        :param values: 一个字典，包含要更新的选项及其新值

        示例用法：
        
            创建BaseConfig实例
            config = BaseConfig()

            批量更新 [gui] 节下的width和height选项的值
            values_to_update = {'width': 150, 'height': 100}
            config.batch_update_values('gui', values_to_update)
        """
        if not self.config.has_section(section):
            self.config.add_section(section)

        for option, value in values.items():
            # 将所有值转换为字符串
            self.config.set(section, option, str(value))

        self.write_config()
