from .TransparentWindow import TransparentWindow
from PyQt5.QtGui import QColor

class LowerCaseWindow(TransparentWindow):
    def __init__(self):
        super().__init__(text="a", color=QColor(255, 255, 255))