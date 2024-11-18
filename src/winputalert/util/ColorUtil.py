
import re


class ColorUtil:
    """ 
    颜色工具类
    """
    @staticmethod
    def hex_to_rgb(hex_color):
        """
        16进制转RGB

        :param hex_color: 16进制颜色值，例如 "#900abf"

        :return: RGB颜色值，例如 (0, 0, 0)

        :raises ValueError: 如果输入的16进制颜色值格式不正确

        :example:

        >>> hex_to_rgb("#900abf")

        获取返回值的方式

        >>> r, g, b = hex_to_rgb("#900abf")
        或者
        >>> rgb = hex_to_rgb("#900abf")
        或者
        >>> r = hex_to_rgb("#900abf")[0]
        或者
        >>> g = hex_to_rgb("#900abf")[1]
        或者
        >>> b = hex_to_rgb("#900abf")[2]
        """
        match = re.fullmatch(r'#?([0-9a-fA-F]{6})', hex_color)
        if not match:
            raise ValueError("Invalid hex color format")
        hex_color = match.group(1)
        r, g, b = int(hex_color[0:2], 16), int(
            hex_color[2:4], 16), int(hex_color[4:6], 16)
        return r, g, b
