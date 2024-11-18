from winputalert.config.BaseConfig import BaseConfig


class GUIConfig(BaseConfig):
    """ GUI的配置类 """

    def __init__(self):
        # 调用父类构造函数，config_file 由 BaseConfig 默认值传入
        super().__init__()

    def get_gui_width(self):
        """ 
        获取GUI的宽度
        """
        return self.config.getint('gui', 'width', fallback=None)

    def get_gui_height(self):
        """ 
        获取GUI的高度
        """
        return self.config.getint('gui', 'height', fallback=None)

    def get_gui_font(self):
        """ 
        获取GUI的字体
        """
        return self.config.get('gui', 'font', fallback=None)

    def get_gui_font_size(self):
        """ 
        获取GUI的字体大小
        """
        return self.config.getint('gui', 'font_size', fallback=None)

    # def get_gui_font_color(self):
    #     """
    #     获取GUI的字体颜色
    #     """
    #     return self.config.get('gui', 'font_color', fallback=None)

    def get_gui_font_color_r(self):
        """
        获取GUI的字体颜色的R值
        """
        return self.config.getint('gui', 'font_color_r', fallback=None)

    def get_gui_font_color_g(self):
        """
        获取GUI的字体颜色的G值
        """
        return self.config.getint('gui', 'font_color_g', fallback=None)

    def get_gui_font_color_b(self):
        """
        获取GUI的字体颜色的B值
        """
        return self.config.getint('gui', 'font_color_b', fallback=None)

    def get_gui_pos(self):
        """ 
        获取GUI的位置
        """
        return self.config.get('gui', 'pos', fallback=None)

    def get_bg_color_r(self):
        """ 
        获取GUI的背景颜色的R值
        """
        return self.config.getint('gui', 'bg_color_r', fallback=None)

    def get_bg_color_g(self):
        """
        获取GUI的背景颜色的G值
        """
        return self.config.getint('gui', 'bg_color_g', fallback=None)

    def get_bg_color_b(self):
        """
        获取GUI的背景颜色的B值
        """
        return self.config.getint('gui', 'bg_color_b', fallback=None)

    def get_gui_opacity(self):
        """ 
        获取GUI的不透明度
        """
        return self.config.getfloat('gui', 'opacity', fallback=None)

    def get_gui_border_radius(self):
        """ 
        获取GUI的边框圆角
        """
        return self.config.getint('gui', 'border_radius', fallback=None)

    def get_gui_delay_close_time(self):
        """
        获取GUI延时关闭时间
        """
        return self.config.getint("gui", "gui_delay_close_time", fallback=None)

    def set_gui_width(self, value):
        """
        设置GUI的宽度

        :param value: 要设置的宽度值
        """
        self.config.set('gui', 'width', str(value))
        self.write_config()

    def set_gui_height(self, value):
        """
        设置GUI的高度

        :param value: 要设置的高度值
        """
        self.config.set('gui', 'height', str(value))
        self.write_config()

    def set_gui_font(self, value):
        """
        设置GUI的字体

        :param value: 要设置的字体值
        """
        self.config.set('gui', 'font', value)
        self.write_config()

    def set_gui_font_size(self, value):
        """
        设置GUI的字体大小

        :param value: 要设置的字体大小值
        """
        self.config.set('gui', 'font_size', str(value))
        self.write_config()

    def set_gui_font_color_r(self, value):
        """
        设置GUI的字体颜色的R值

        :param value: 要设置的R值
        """
        self.config.set('gui', 'font_color_r', str(value))
        self.write_config()

    def set_gui_font_color_g(self,
                            value):
        """
        设置GUI的字体颜色的G值

        :param value: 要设置的G值
        """
        self.config.set('gui', 'font_color_g', str(value))
        self.write_config()

    def set_gui_font_color_b(self, value):
        """
        设置GUI的字体颜色的B值

        :param value: 要设置的B值
        """
        self.config.set('gui', 'font_color_b', str(value))
        self.write_config()

    def set_gui_pos(self, value):
        """
        设置GUI的位置

        :param value: 要设置的位置值
        """
        self.config.set('gui', 'pos', value)
        self.write_config()

    def set_bg_color_r(self, value):
        """
        设置GUI的背景颜色的R值

        :param value: 要设置的R值
        """
        self.config.set('gui', 'bg_color_r', str(value))
        self.write_config()

    def set_bg_color_g(self, value):
        """
        设置GUI的背景颜色的G值

        :param value: 要设置的G值
        """
        self.config.set('gui', 'bg_color_g', str(value))
        self.write_config()

    def set_bg_color_b(self, value):
        """
        设置GUI的背景颜色的B值

        :param value: 要设置的B值
        """
        self.config.set('gui', 'bg_color_b', str(value))
        self.write_config()

    def set_gui_opacity(self, value):
        """
        设置GUI的不透明度

        :param value: 要设置的不透明度值
        """
        self.config.set('gui', 'opacity', str(value))
        self.write_config()

    def set_gui_border_radius(self, value):
        """
        设置GUI的边框圆角

        :param value: 要设置的边框圆角值
        """
        self.config.set('gui', 'border_radius', str(value))
        self.write_config()

    def set_gui_delay_close_time(self, value):
        """
        设置GUI延时关闭时间

        :param value: 要设置的延时关闭时间值
        """
        self.config.set("gui", "gui_delay_close_time", str(value))
        self.write_config()