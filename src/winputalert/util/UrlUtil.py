import webbrowser


class UrlUtil:
    """ 
    url 工具类
    """
    def __init__(self):
        pass

    @staticmethod
    def open_url(url: str):
        # 使用默认浏览器打开URL
        webbrowser.open(url)
