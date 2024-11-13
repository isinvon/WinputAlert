from .TransparentWindow import TransparentWindow
from PyQt5.QtGui import QColor

class EnglishWindow(TransparentWindow):
    def __init__(self):
        # super().__init__(text="英", color=QColor(255, 255, 255))
        super().__init__(text="英")
