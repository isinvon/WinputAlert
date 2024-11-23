import os
import shutil
from platformdirs import user_data_dir


class ConfigFileManager:
    """ 
    配置文件工具类，将配置文件拷贝到用户数据目录下
    
    使用此工具类的原因: 在 Program Files 下的权限受限，比如文件的覆盖、拷贝、写入都会受到限制
    """
    def __init__(self):
        self.app_name = "WinputAlert"
        self.app_author = os.getlogin()  # 获取当前登录的用户名

        # 自动获取当前用户的 AppData 数据目录
        self.user_data_dir = user_data_dir(appname=self.app_name, appauthor=self.app_author)

        # 配置文件路径
        self.config_ini_path = os.path.join(self.user_data_dir, "config.ini")
        self.config_ini_bak_path = os.path.join(self.user_data_dir, "config.ini.bak.original")

        # 程序安装目录（假设配置文件原始位置）
        self.install_dir = os.path.dirname(os.path.abspath(__file__))
        self.source_config_ini = os.path.join(self.install_dir, "config.ini")
        self.source_config_ini_bak = os.path.join(self.install_dir, "config.ini.bak.original")

    def initialize_user_config(self):
        """
        将配置文件拷贝到用户数据目录，并确保拷贝文件存在
        :return: 如果文件成功拷贝并存在于目标目录中，返回 True，否则返回 False
        """
        try:
            # 确保用户数据目录存在
            os.makedirs(self.user_data_dir, exist_ok=True)

            # 拷贝文件并验证是否存在
            if not os.path.exists(self.config_ini_path):
                shutil.copy(self.source_config_ini, self.config_ini_path)

            if not os.path.exists(self.config_ini_bak_path):
                shutil.copy(self.source_config_ini_bak, self.config_ini_bak_path)

            # 检查拷贝后的文件是否存在
            config_exists = os.path.exists(self.config_ini_path)
            bak_exists = os.path.exists(self.config_ini_bak_path)

            # 如果所有文件都存在，返回 True，否则返回 False
            return config_exists and bak_exists

        except Exception as e:
            print(f"初始化配置文件失败：{e}")
            return False

    def get_config_file_paths(self):
        """
        返回用户目录中配置文件的路径
        :return: 一个字典，包含 `config.ini` 和 `config.ini.bak.original` 的路径
        """
        return {
            "config_ini": self.config_ini_path,
            "config_ini_bak": self.config_ini_bak_path
        }
