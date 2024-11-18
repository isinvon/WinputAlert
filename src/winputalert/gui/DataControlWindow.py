import os
import shutil

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QColor, QFont, QFontDatabase, QIcon
from PySide6.QtWidgets import (QApplication, QCheckBox, QColorDialog,
                               QComboBox, QFormLayout, QHBoxLayout, QLabel,
                               QLineEdit, QMainWindow, QMessageBox, QDoubleSpinBox,
                               QPushButton, QVBoxLayout, QWidget)

from winputalert.config.animation_config.BaseAnimationConfig import \
    BaseAnimationConfig
from winputalert.config.animation_config.BounceAnimationConfig import \
    BounceAnimationConfig
from winputalert.config.animation_config.FadeInAnimationConfig import \
    FadeInAnimationConfig
from winputalert.config.animation_config.ScaleUpAnimationConfig import \
    ScaleUpAnimationConfig
from winputalert.config.animation_config.SlideInAnimationConfig import \
    SlideInAnimationConfig
from winputalert.config.AppInfoConfig import AppInfoConfig
from winputalert.config.GUIConfig import GUIConfig
from winputalert.config.KeyboardConfig import KeyboardConfig
from winputalert.config.SystemConfig import SystemConfig
from winputalert.gui.data_control_window_component.ColorPickerButton import \
    ColorPickerButton
from winputalert.gui.data_control_window_component.RoundedSpinbox import \
    RoundedSpinBox


class DataControlWindow(QWidget):
    """
    数据控制窗口类，支持自定义宽高、字体、颜色等界面属性。
    """

    global gui_config, keyboard_config, system_config, app_info_config, base_animation_config, bounce_animation_config, fade_in_animation_config, scale_up_animation_config, slide_in_animation_config

    gui_config = GUIConfig()
    keyboard_config = KeyboardConfig()
    system_config = SystemConfig()
    app_info_config = AppInfoConfig()
    base_animation_config = BaseAnimationConfig()
    bounce_animation_config = BounceAnimationConfig()
    fade_in_animation_config = FadeInAnimationConfig()
    scale_up_animation_config = ScaleUpAnimationConfig()
    slide_in_animation_config = SlideInAnimationConfig()

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

        # 设置下拉框样式
        self.setStyleSheet("""
            QComboBox {
                font-size: 14px;  /* 设置字体大小 */
                padding: 4px 8px;  /* 内边距 */
            }
            QComboBox QAbstractItemView {
                font-size: 12px;  /* 下拉选项字体大小 */
                selection-background-color: #38749c;  /* 选中项背景颜色 */
                selection-color: white;  /* 选中项字体颜色 */
                padding: 4px;  /* 调整选项的内边距 */
            }
        """)

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
        self.width_input.setMinimum(5)  # 设置最小值（假设最小值为 5）
        self.width_input.setMaximum(1000)  # 设置最大值（假设最大值为 1000）
        self.width_input.setValue(gui_config.get_gui_width())  # 显示配置中的值
        self.width_input.setFont(common_font)
        form_layout.addRow("宽度(5-1000):", self.width_input)

        # 高度设置
        self.height_input = RoundedSpinBox(self)
        self.height_input.setMinimum(5)  # 设置最小值（假设最小值为 5）
        self.height_input.setMaximum(1000)  # 设置最大值（假设最大值为 1000）
        self.height_input.setValue(gui_config.get_gui_height())  # 显示配置中的值·
        self.height_input.setFont(common_font)
        form_layout.addRow("高度(5-1000):", self.height_input)

        # 字体选择
        self.font_input = QComboBox(self)
        self.font_input.setFont(common_font)
        # self.font_input.setStyleSheet(input_style)
        families_list = QFontDatabase.families()  # 获取系统上所有可用的字体列表
        self.font_input.addItems(families_list)  # 向下拉框中添加字体列表
        if gui_config.get_gui_font() in families_list:  # 确保配置中的字体存在于系统字体列表中
            self.font_input.setCurrentText(gui_config.get_gui_font())  # 设置默认字体
        form_layout.addRow("字体:", self.font_input)

        # 字体大小设置
        self.font_size_input = RoundedSpinBox(self)
        self.font_size_input.setMinimum(1)
        self.font_size_input.setMaximum(500)
        self.font_size_input.setValue(
            gui_config.get_gui_font_size())  # 显示配置中的值
        self.font_size_input.setFont(common_font)
        form_layout.addRow("字体大小(1-500):", self.font_size_input)

        # 边框圆角设置
        self.border_radius_input = RoundedSpinBox(self)
        self.border_radius_input.setMinimum(0)
        self.border_radius_input.setMaximum(100)
        self.border_radius_input.setValue(
            gui_config.get_gui_border_radius())  # 显示配置中的值
        self.border_radius_input.setFont(common_font)
        form_layout.addRow("边框圆角(0-100):", self.border_radius_input)

        # 不透明度设置
        # 使用 QDoubleSpinBox 代替 RoundedSpinBox
        self.opacity_input = QDoubleSpinBox(self)
        self.opacity_input.setRange(0.1, 1.0)  # 范围设置为 0.1 到 1.0
        self.opacity_input.setSingleStep(0.1)  # 每次步进增加 0.1
        self.opacity_input.setDecimals(1)  # 显示 1 位小数
        self.opacity_input.setValue(gui_config.get_gui_opacity())  # 显示配置中的值
        self.opacity_input.setFont(common_font)
        self.opacity_input.setStyleSheet("""
             QDoubleSpinBox {
                font-size: 14px;  /* 设置字体大小 */
                padding: 4px 4px;  /* 内边距 */
                border: 1px solid #ccc;  /* 边框颜色 */
                border-radius: 6px;  /* 圆角 */
            }
            QDoubleSpinBox::up-button, QDoubleSpinBox::down-button {
                width: 12px;  /* 调节按钮宽度 */
                border: none;  /* 去除边框 */
                border-radius: 4px;  /* 调节按钮圆角 */
                background-color: #cad6db;  /* 调节按钮背景颜色 */
                padding: 2px;  /* 内边距 */
            }
            QDoubleSpinBox::up-button:hover, QDoubleSpinBox::down-button:hover {
                background-color: #606669;  /* 鼠标悬停时背景颜色 */
            }
            QDoubleSpinBox::up-button:pressed, QDoubleSpinBox::down-button:pressed {
                background-color: #38749c;  /* 按下时背景颜色 */
            }
            QDoubleSpinBox::up-arrow, QDoubleSpinBox::down-arrow {
                width: 8px;  /* 箭头宽度 */
                height: 8px;  /* 箭头高度 */
            }
        """)
        form_layout.addRow("不透明度(0-1):", self.opacity_input)

        # GUI位置设置 ===================开始===================================
        self.pos_input = QComboBox(self)
        self.pos_input.setFont(common_font)
        # 中英文位置映射
        positions_map = {
            "左上": "top_left", "上中": "top_center", "右上": "top_right",
            "左中": "left_center", "中间": "center", "右中": "right_center",
            "左下": "bottom_left", "中下": "bottom_center", "右下": "bottom_right"
        }
        # 添加选项（中文显示，英文绑定值）
        self.pos_input.addItems(positions_map.keys())  # 添加中文显示
        for index, (chinese, english) in enumerate(positions_map.items()):
            self.pos_input.setItemData(index, english)  # 绑定英文值到每个选项

        # 设置默认值为当前配置的英文位置
        current_position = gui_config.get_gui_pos()
        if current_position in positions_map.values():
            self.pos_input.setCurrentIndex(
                list(positions_map.values()).index(current_position)
            )

        # 添加信号（响应下拉框选择变化）
        self.pos_input.currentIndexChanged.connect(
            lambda: print(f"选中的英文位置：{self.pos_input.currentData()}")
        )

        form_layout.addRow("位置:", self.pos_input)
        # GUI位置设置 ===================结束===================================

        # TODO 动画类型设置 (未映射config.ini中的值)
        self.animation_type_input = QComboBox(self)
        self.animation_type_input.setFont(common_font)
        # TODO 建议修改为"淡入","抖动(强)","抖动(中)","抖动(弱)","放大(强)","放大(中)","放大(弱)","滑入(从左向右)","滑入(从右到左)","滑入(从上往下)","滑入(从下往上)",然后他们共用一个动画持续时间
        animations = ["淡入", "抖动(强)", "抖动(中)", "抖动(弱)", "放大(强)", "放大(中)",
                      "放大(弱)", "滑入(从左向右)", "滑入(从右到左)", "滑入(从上往下)", "滑入(从下往上)"]
        # animations = ["淡入(fade_in)", "弹动(bounce)", "抖动(shake)", "放大(scale_up)", "滑入(slide_in)"]
        self.animation_type_input.addItems(animations)
        form_layout.addRow("动画类型:", self.animation_type_input)

        # !!键盘检测时间设置 (不对用户开放修改)
        # self.keyboard_interval_input = RoundedSpinBox(self)
        # self.keyboard_interval_input.setValue(1)
        # self.keyboard_interval_input.setFont(common_font)
        # form_layout.addRow("键盘检测间隔 (Keyboard Interval):",
        #                    self.keyboard_interval_input)

        # 开机启动选择 ========================开始===============================
        self.is_startup_input = QComboBox(self)
        self.is_startup_input.setFont(common_font)

        # 中英映射：显示值 -> 数据值
        start_up_option = {
            "是": True,
            "否": False
        }

        # 添加选项和绑定数据
        for index, (text, value) in enumerate(start_up_option.items()):
            self.is_startup_input.addItem(text)
            self.is_startup_input.setItemData(index, value)  # 绑定数据值

        # 设置默认值
        current_startup = system_config.get_auto_start_on_system_boot()
        if current_startup in start_up_option.values():
            self.is_startup_input.setCurrentIndex(
                list(start_up_option.values()).index(current_startup)
            )

        # 添加信号（响应下拉框选择变化）
        self.is_startup_input.currentIndexChanged.connect(
            lambda: print(f"选中的位置：{self.is_startup_input.currentData()}")
        )

        form_layout.addRow("是否开机启动:", self.is_startup_input)
        # 开机启动选择 ========================结束===============================

        # 字体颜色选择
        # self.font_color = QColor(0, 0, 0)  # 初始化颜色, 默认字体颜色（黑色）
        # self.font_color_button = ColorPickerButton(
        #     "选择字体颜色", self.select_font_color, self)
        # form_layout.addRow("字体颜色 (Font Color):", self.font_color_button)

        # 字体颜色选择 =====================开始====================================
        gui_config.get_gui_font_color_r()

        # self.font_color = QColor(0, 0, 0)  # 初始化颜色, 默认字体颜色（黑色）
        self.font_color = QColor(
            gui_config.get_gui_font_color_r(),
            gui_config.get_gui_font_color_b(),
            gui_config.get_gui_font_color_g()
        )
        # 创建按钮并设置背景颜色
        self.font_color_button = ColorPickerButton(
            "选择字体颜色", self.select_font_color, self
        )
        # 设置默认颜色为字体颜色
        self.update_font_color_button_style()
        form_layout.addRow("字体颜色:", self.font_color_button)
        # 字体颜色选择 =====================结束====================================

        # 背景颜色选择======================开始====================================
        # self.bg_color = QColor(255, 255, 255)  # 初始化颜色，默认背景颜色（白色）
        self.bg_color = QColor(
            gui_config.get_bg_color_r(),
            gui_config.get_bg_color_b(),
            gui_config.get_bg_color_g()
        )
        self.bg_color_button = ColorPickerButton(
            "选择背景颜色", self.select_bg_color, self
        )

        # 设置默认颜色为背景颜色
        self.update_bg_color_button_style()

        form_layout.addRow("背景颜色:", self.bg_color_button)
        # 背景颜色选择======================结束====================================

        # 保存按钮和重置按钮并列
        button_layout = QHBoxLayout()  # 创建水平布局

        # 重置按钮
        self.reset_button = QPushButton("重置设置", self)
        self.reset_button.setFont(common_font)
        self.reset_button.setStyleSheet("""
            QPushButton {
                background-color: #e77063;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 8px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #f58276;
            }
        """)
        self.reset_button.clicked.connect(self.reset_configuration)
        button_layout.addWidget(self.reset_button)  # 将重置按钮添加到水平布局

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
        button_layout.addWidget(self.save_button)  # 将重置按钮添加到水平布局
        layout.addLayout(button_layout)  # 将按钮的水平布局添加到主布局

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
        color_dialog = QColorDialog(
            self.font_color, self)  # 创建颜色选择对话框，初始颜色为当前颜色
        selected_color = color_dialog.getColor()

        if selected_color.isValid():  # 如果用户选择了有效颜色
            self.font_color = selected_color
            self.update_font_color_button_style()

    def update_font_color_button_style(self):
        """ 
        更新字体颜色按钮样式
        """
        # 判断颜色亮度
        luminance = (self.font_color.red() * 0.299 +
                     self.font_color.green() * 0.587 +
                     self.font_color.blue() * 0.114)
        font_color_text = "white" if luminance < 128 else "black"  # 根据亮度选择字体颜色

        # 更新按钮样式
        self.font_color_button.setStyleSheet(f"""
            QPushButton {{
                background-color: {self.font_color.name()};  /* 背景色为选择颜色 */
                color: {font_color_text};  /* 根据亮度设置字体颜色 */
                border: none;
                border-radius: 5px;
                padding: 8px;
            }}
        """)

    def select_bg_color(self):
        """
        选择背景颜色
        """
        color = QColorDialog.getColor(
            self.bg_color, self)  # 创建颜色选择对话框，初始颜色为当前背景色
        if color.isValid():  # 如果选择了有效颜色
            self.bg_color = color  # 更新背景颜色
            self.update_bg_color_button_style()  # 更新按钮样式

    def update_bg_color_button_style(self):
        # 判断颜色亮度
        luminance = (self.bg_color.red() * 0.299 +
                     self.bg_color.green() * 0.587 +
                     self.bg_color.blue() * 0.114)
        font_color_text = "white" if luminance < 128 else "black"  # 根据亮度选择字体颜色

        # 更新按钮样式
        self.bg_color_button.setStyleSheet(f"""
            QPushButton {{
                background-color: {self.bg_color.name()};  /* 背景色为选择颜色 */
                color: {font_color_text};  /* 根据亮度设置字体颜色 */
                border: none;
                border-radius: 5px;
                padding: 8px;
            }}
        """)

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

    def reset_configuration(self):
        """
        重置默认配置

        原理: 将config.ini.bak配置文件覆盖config.ini
        """
        # 直接将config.ini.bak.original文件拷贝覆盖config.ini
        configini_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "..",
            "config",
            'config.ini'
        )
        # 获取config.ini.bak.original的路径
        configini_bak_original_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "..",
            "config",
            'config.ini.bak.original'

        )
        try:
            # 直接将 config.ini.bak.original 文件拷贝覆盖 config.ini
            shutil.copy(configini_bak_original_path, configini_path)
            QMessageBox.information(self, "重置成功", "配置已成功重置为默认值！")
        except FileNotFoundError:
            QMessageBox.warning(self, "重置失败", "配置文件不存在，无法重置！")
        except Exception as e:
            QMessageBox.critical(self, "重置失败", f"重置配置时发生错误: {e}")

    # 重写关闭事件（此方法不需要调用，重写之后会自动使用）点击关闭按钮时隐藏窗口而不是退出程序（不然会导致托盘和输入法状态GUI同时被关闭）
    def closeEvent(self, event):
        """ 点击关闭按钮时隐藏窗口而不是退出程序 """
        event.ignore()  # 阻止默认关闭事件
        self.hide()  # 隐藏窗口
