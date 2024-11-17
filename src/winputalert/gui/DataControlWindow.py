import os

from PySide6.QtGui import QColor, QFont, QFontDatabase, QIcon
from PySide6.QtWidgets import (QApplication, QColorDialog, QComboBox,
                               QFormLayout, QPushButton, QVBoxLayout, QWidget)

from winputalert.gui.data_control_window_component.ColorPickerButton import \
    ColorPickerButton
from winputalert.gui.data_control_window_component.RoundedSpinbox import \
    RoundedSpinBox


class DataControlWindow(QWidget):
    """
    数据控制窗口类，支持自定义宽高、字体、颜色等界面属性。
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("WinputAlert")  # 设置窗口标题
        # 获取图标的绝对路径
        current_path = os.path.abspath(__file__)
        current_dir = os.path.dirname(current_path)
        ico_path = os.path.join(
            current_dir, "..", "resources", "WinputAlert.ico")
        # 设置窗口图标
        self.setWindowIcon(QIcon(ico_path))
        self.setGeometry(100, 100, 500, 400)  # 设置窗口大小和位置
        self.setStyleSheet("background-color: #f8f9fa;")  # 设置窗口背景为浅色

        # 设置窗口大小(不允许改变大小,写死了大小)
        # self.setFixedSize(400, 400)

        # 计算并设置窗口居中显示
        self.center()

        self.init_ui()  # 初始化UI组件

    def init_ui(self):
        layout = QVBoxLayout(self)
        form_layout = QFormLayout()

        common_font = QFont("Microsoft YaHei", 12)

        # 宽度设置
        self.width_input = RoundedSpinBox(self)
        self.width_input.setValue(120)
        self.width_input.setFont(common_font)
        form_layout.addRow("宽度 (Width):", self.width_input)

        # 高度设置
        self.height_input = RoundedSpinBox(self)
        self.height_input.setValue(90)
        self.height_input.setFont(common_font)
        form_layout.addRow("高度 (Height):", self.height_input)

        # 字体选择
        self.font_input = QComboBox(self)
        self.font_input.setFont(common_font)
        # self.font_input.setStyleSheet(input_style)
        # 获取系统上所有可用的字体列表
        families_list = QFontDatabase.families()
        # 向下拉框中添加字体列表
        self.font_input.addItems(families_list)
        form_layout.addRow("字体 (Font):", self.font_input)

        # 字体大小设置
        self.font_size_input = RoundedSpinBox(self)
        self.font_size_input.setValue(14)
        self.font_size_input.setFont(common_font)
        form_layout.addRow("字体大小 (Font Size):", self.font_size_input)

        # 字体颜色选择
        self.font_color = QColor(0, 0, 0)  # 初始化颜色, 默认字体颜色（黑色）
        self.font_color_button = ColorPickerButton(
            "选择字体颜色", self.select_font_color, self)
        form_layout.addRow("字体颜色 (Font Color):", self.font_color_button)

        # 背景颜色选择
        self.bg_color = QColor(255, 255, 255)  # 初始化颜色，默认背景颜色（白色）
        self.bg_color_button = ColorPickerButton(
            "选择背景颜色", self.select_bg_color, self)
        form_layout.addRow("背景颜色 (Background Color):", self.bg_color_button)

        # 保存按钮
        self.save_button = QPushButton("保存设置", self)
        self.save_button.setFont(common_font)
        self.save_button.setStyleSheet("""
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
        self.save_button.clicked.connect(self.save_configuration)
        layout.addLayout(form_layout)
        layout.addWidget(self.save_button)

    def center(self):
        """ 窗口居中显示 """
        # 获取屏幕的分辨率
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()

        # 获取窗口的宽高
        window_width = self.width()
        window_height = self.height()

        # 计算窗口的左上角位置，使其居中
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # 设置窗口位置
        self.move(x, y)

    def select_font_color(self):
        """ 
        选择字体颜色
        """
        color = QColorDialog.getColor()
        if color.isValid():
            self.font_color = color  # 直接更新 font_color
            self.font_color_button.update_color(color)  # 更新按钮显示

    def select_bg_color(self):
        """
        选择背景颜色
        """
        color = QColorDialog.getColor()
        if color.isValid():
            self.bg_color = color  # 直接更新 bg_color
            self.bg_color_button.update_color(color)  # 更新按钮显示

    def save_configuration(self):
        """
        保存配置
        """
        config = {
            "width": self.width_input.value(),
            "height": self.height_input.value(),
            "font": self.font_input.currentText(),
            "font_size": self.font_size_input.value(),
            "font_color": self.font_color.name(),  # 保存字体颜色的Hex值
            "bg_color": self.bg_color.name()  # 保存背景颜色的Hex值
        }
        print("保存的配置:", config)
        return config  # 返回配置，包括颜色

    # 重写关闭事件（此方法不需要调用，重写之后会自动使用）点击关闭按钮时隐藏窗口而不是退出程序（不然会导致托盘和输入法状态GUI同时被关闭）
    def closeEvent(self, event):
        """ 点击关闭按钮时隐藏窗口而不是退出程序 """
        event.ignore()  # 阻止默认关闭事件
        self.hide()  # 隐藏窗口


# if __name__ == "__main__":
#     app = QApplication([])
#     window = DataControlWindow()
#     window.show()
#     app.exec()
