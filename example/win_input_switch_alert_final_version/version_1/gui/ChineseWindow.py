from .TransparentWindow import TransparentWindow
from PyQt5.QtGui import QColor

class ChineseWindow(TransparentWindow):
    def __init__(self):
        super().__init__(text="中", color=QColor(255, 255, 255))
        