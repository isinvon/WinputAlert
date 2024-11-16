from winputalert.config.BaseConfig import BaseConfig


class AppInfoConfig(BaseConfig):
    """ app 信息的配置类 """

    def __init__(self):
        # 调用父类构造函数，config_file 由 BaseConfig 默认值传入
        super().__init__()

    def get_app_author(self):
        """
        获取app的作者
        """
        return self.config.get('app_info', 'author', fallback=None)

    def get_app_version(self):
        """
        获取app的版本
        """
        return self.config.get('app_info', 'version', fallback=None)

    def get_app_name(self):
        """
        获取app的项目名称
        """
        return self.config.get('app_info', 'app_name', fallback=None)

    def get_official_website_address(self):
        """
        获取app的项目官网地址
        """
        return self.config.get('app_info', 'official_website_address', fallback=None)

    def get_app_desc(self):
        """
        获取app的项目描述
        """
        return self.config.get('app_info', 'app_desc', fallback=None)

    def get_project_doc(self):
        """
        获取app的文档地址
        """
        return self.config.get('app_info', 'project_doc', fallback=None)

    def get_project_link(self):
        """
        获取app的项目地址
        """
        return self.config.get('app_info', 'project_link', fallback=None)

    def get_email(self):
        """
        获取联系支持的邮箱
        """
        return self.config.get('app_info', 'email', fallback=None)

    def get_copyright(self):
        """
        获取版权信息
        """
        return self.config.get('app_info', 'copyright', fallback=None)

    def set_app_author(self, value):
        """
        设置app的作者

        :param value: 要设置的作者值
        """
        self.config.set('app_info', 'author', value)
        self.write_config()

    def set_app_version(self, value):
        """
        设置app的版本

        :param value: 要设置的版本值
        """
        self.config.set('app_info', 'version', value)
        self.write_config()

    def set_app_name(self, value):
        """
        设置app的项目名称

        :param value: 要设置的项目名称值
        """
        self.config.set('app_info', 'app_name', value)
        self.write_config()

    def set_official_website_address(self, value):
        """
        设置app的项目官网地址

        :param value: 要设置的项目官网地址值
        """
        self.config.set('app_info', 'official_website_address', value)
        self.write_config()

    def set_app_desc(self, value):
        """
        设置app的项目描述

        :param value: 要设置的项目描述值
        """
        self.config.set('app_info', 'app_desc', value)
        self.write_config()

    def set_project_doc(self,
                        value):
        """
        设置app的文档地址

        :param value: 要设置的文档地址值
        """
        self.config.set('app_info', 'project_doc', value)
        self.write_config()

    def set_project_link(self, value):
        """
        设置app的项目地址

        :param value: 要设置的项目地址值
        """
        self.config.set('app_info', 'project_link', value)
        self.write_config()

    def set_email(self, value):
        """
        设置联系支持的邮箱

        :param value: 要设置的邮箱值
        """
        self.config.set('app_info', 'email', value)
        self.write_config()

    def set_copyright(self, value):
        """
        设置版权信息

        :param value: 要设置的版权信息值
        """
        self.config.set('app_info', 'copyright', value)
        self.write_config()