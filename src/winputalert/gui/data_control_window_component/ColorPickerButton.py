from PySide6.QtWidgets import QPushButton


class ColorPickerButton(QPushButton):
    """
    自定义的颜色选择按钮。
    """

    def __init__(self, text, callback, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("""
            QPushButton {
                background-color: #38749c;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 8px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #3e7fab;
            }
        """)
        self.clicked.connect(callback)

    def update_color(self, color):
        """
        更新按钮的背景颜色，并根据颜色计算合适的文字颜色。
        """
        text_color = self.get_contrasting_color(color)
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {color.name()};
                color: {text_color};
                border: none;
                border-radius: 8px;
                padding: 8px;
                font-size: 14px;
            }}
        """)

    def get_contrasting_color(self, color):
        """
        根据颜色亮度获取对比色（黑色或白色）。
        """
        brightness = (color.red() * 0.299 + color.green()
                      * 0.587 + color.blue() * 0.114)
        return "white" if brightness < 128 else "black"
