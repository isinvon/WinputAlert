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
