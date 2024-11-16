from .TransparentWindow import TransparentWindow
from PyQt5.QtGui import QColor

class UpperCaseWindow(TransparentWindow):
    def __init__(self):
        # super().__init__(text="A", color=QColor(255, 255, 255))
        super().__init__(text="A")
