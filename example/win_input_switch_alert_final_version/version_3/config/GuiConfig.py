from config.BaseConfig import BaseConfig


class GUIConfig(BaseConfig):
    """ GUI的配置类 """

    def __init__(self):
        # 调用父类构造函数，config_file 由 BaseConfig 默认值传入
        super().__init__()

    def get_gui_color(self):
        """ 
        获取GUI的颜色
        """
        return self.config.get('gui', 'color', fallback=None)

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

    def get_gui_font_color(self):
        """ 
        获取GUI的字体颜色
        """
        return self.config.get('gui', 'font_color', fallback=None)

    def get_gui_pos(self):
        """ 
        获取GUI的位置
        """
        return self.config.get('gui', 'pos', fallback=None)

    def get_gui_bg(self):
        """ 
        获取GUI的背景
        """
        return self.config.get('gui', 'bg', fallback=None)

    def get_gui_close_time(self):
        """ 
        获取GUI的关闭时间
        """
        return self.config.getint('gui', 'close_time', fallback=None)

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

    def get_gui_border_shadow(self):
        """ 
        获取GUI的边框阴影
        """
        return self.config.getint('gui', 'border_shadow', fallback=None)

    def get_gui_border_color(self):
        """ 
        获取GUI的边框颜色
        """
        return self.config.get('gui', 'border_color', fallback=None)

    def get_gui_border_size(self):
        """ 
        获取GUI的边框大小
        """
        return self.config.getint('gui', 'border_size', fallback=None)

    def get_gui_border_style(self):
        """ 
        获取GUI的边框样式
        """
        return self.config.getint('gui', 'border_style', fallback=None)

    def get_gui_border_animation(self):
        """ 
        获取GUI的边框动画
        """
        return self.config.getint('gui', 'border_animation', fallback=None)

    def get_gui_border_animation_time(self):
        """ 
        获取GUI的边框动画时间
        """
        return self.config.getint('gui', 'border_animation_time', fallback=None)

    def get_gui_close_time(self):
        """
        获取GUI关闭时间
        """
        return self.config.getint("gui", "gui_close_time", fallback=None)
