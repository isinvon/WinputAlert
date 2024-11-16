import os

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QMenu, QMessageBox, QSystemTrayIcon

from winputalert.config.AppInfoConfig import AppInfoConfig
from winputalert.gui.DataControlWindow import DataControlWindow


class SystemTray(QSystemTrayIcon):

    global app_info_config
    app_info_config = AppInfoConfig()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.main_window = DataControlWindow()
        self.init_tray_icon()

    def init_tray_icon(self):
        current_path = os.path.abspath(__file__)
        current_dir = os.path.dirname(current_path)
        ico_path = os.path.join(
            current_dir, "..", "resources", "WinputAlert.ico")
        self.setIcon(QIcon(ico_path))

        # 创建菜单
        tray_menu = QMenu()

        # 设置菜单项
        settings_action = QAction("设置", self)
        settings_action.triggered.connect(self.show_main_window)
        tray_menu.addAction(settings_action)

        # 菜单分割线
        # tray_menu.addSeparator()

        # 关于菜单项
        about_action = QAction("关于", self)
        about_action.triggered.connect(self.show_about_message)
        tray_menu.addAction(about_action)

        # 帮助菜单项
        # help_action = QAction("帮助", self)
        # help_action.triggered.connect(self.show_help_message)
        # tray_menu.addAction(help_action)

        # 菜单分割线
        # tray_menu.addSeparator()

        # 退出菜单项
        exit_action = QAction("退出", self)
        exit_action.triggered.connect(self.quit_application)
        tray_menu.addAction(exit_action)

        # 扁平化UI风格的菜单样式 (暗色系)
        # tray_menu.setStyleSheet(
        #     "QMenu { background-color: #2c3e50; border-radius: 5px; padding: 5px; }"
        #     "QMenu::item { padding: 10px; color: #ecf0f1; }"
        #     "QMenu::item:selected { background-color: #4e92bf; color: white; }"
        #     "QMenu::item:!selected { background-color: transparent; }"
        # )

        # 扁平化UI风格的菜单样式 (亮色系)
        tray_menu.setStyleSheet(
            "QMenu { background-color: #ffffff; border-radius: 5px; padding: 5px; }"
            "QMenu::item { padding: 6px; color: #333333; font-weight: bold;}"
            # 选中的菜单项的样式，color 是选中时候字体颜色
            "QMenu::item:selected { background-color: #4e92bf; color: white; }"
            "QMenu::item:!selected { background-color: transparent; }"
        )

        # 设置菜单为托盘菜单
        self.setContextMenu(tray_menu)
        self.setVisible(True)
        self.activated.connect(self.on_tray_icon_activated)

    def show_about_message(self):
        """显示关于信息"""
        about_box = QMessageBox(self.main_window)
        about_box.setWindowTitle("关于")

        app_name = app_info_config.get_app_name()
        app_dec = app_info_config.get_app_desc()
        app_version = app_info_config.get_app_version()
        app_author = app_info_config.get_app_author()
        app_official_website_address = app_info_config.get_official_website_address()
        app_support_email = app_info_config.get_email()
        app_copyright = app_info_config.get_copyright()

        # 使用 HTML 格式化文本
        about_text = f"""
        <div style="text-align: left;">
            <h2 style="color: #3498db; margin-bottom: 10px;"> {app_name}</h2>
            <p> {app_dec}</p>
            <p><strong>版本:</strong> {app_version}</p>
            <p><strong>作者:</strong> {app_author}</p>
            <p><strong>官网:</strong> <a href="{app_official_website_address}" style="color: #3498db;"> {app_official_website_address}</a></p>
            <p><strong>支持:</strong> <a href="{app_support_email}" style="color: #3498db;"> {app_support_email}</a></p>
            <p><strong>版权声明:</strong> {app_copyright}</p>
        </div>
        """
        about_box.setTextFormat(Qt.RichText)  # 支持 HTML 格式
        about_box.setText(about_text)
        about_box.setIcon(QMessageBox.Information)
        # about_box.setStandardButtons(QMessageBox.Ok)
        about_box.setStandardButtons(QMessageBox.Close)
        about_box.setWindowModality(Qt.ApplicationModal)

        # 修改关闭按钮的文本(从"Close" -> "关闭")
        close_button = about_box.button(QMessageBox.Close)
        close_button.setText("关闭")

        # 设置窗口样式
        about_box.setStyleSheet("""
            QMessageBox {
                background-color: rgba(255, 255, 255, 0.95);
                border-radius: 10px;
                padding: 15px;
            }
            QMessageBox QLabel {
                font-family: Arial, sans-serif;
                font-size: 14px;
                line-height: 1.6;
            }
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 8px;
                margin: 5px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #1d6fa5;
            }
        """)

        about_box.exec()

    # def show_help_message(self):
    #     """显示帮助信息"""

    #     # 创建一个 QMessageBox 实例
    #     help_box = QMessageBox(self.main_window)
    #     help_box.setWindowTitle("帮助")

    #     app_name = app_info_config.get_app_name()
    #     app_dec = app_info_config.get_app_desc()
    #     app_version = app_info_config.get_app_version()
    #     app_author = app_info_config.get_app_author()
    #     app_official_website_address = app_info_config.get_official_website_address()
    #     app_project_doc = app_info_config.get_project_doc()
    #     app_support_email = app_info_config.get_email()
    #     app_copyright = app_info_config.get_copyright()

    #     # 使用 HTML 格式化文本
    #     help_text = f"""
    #     <div style="text-align: left;">
    #         <h2 style="color: #3498db; margin-bottom: 10px;">帮助文档</h2>
    #         <p>如果您需要帮助，请点击以下链接：</p>
    #         <p style="color: #2c3e50; font-size: 14px;">
    #             <strong>文档地址:</strong>
    #             <a href="{app_project_doc}" style="color: #3498db; text-decoration: none;"> {app_project_doc}</a>
    #         </p>
    #         <p style="color: #2c3e50; font-size: 14px;">
    #             <strong>联系支持:</strong>
    #             <a href="{app_support_email}" style="color: #3498db; text-decoration: none;"> {app_support_email}</a>
    #         </p>
    #         <p style="color: #2c3e50; font-size: 14px;">
    #             <strong>版权声明:</strong> {app_copyright}
    #         </p>
    #     </div>
    #     """
    #     help_box.setTextFormat(Qt.RichText)  # 支持 HTML 格式
    #     help_box.setText(help_text)
    #     help_box.setIcon(QMessageBox.Icon.Information)
    #     # 设置关闭按钮
    #     help_box.setStandardButtons(QMessageBox.Close)
    #     help_box.setWindowModality(Qt.ApplicationModal)

    #     # 修改帮助按钮的文本
    #     close_button = help_box.button(QMessageBox.Close)
    #     close_button.setText("关闭")

    #     # 设置窗口样式
    #     help_box.setStyleSheet("""
    #         QMessageBox {
    #             background-color: rgba(255, 255, 255, 0.9);
    #             border-radius: 10px;
    #             padding: 15px;
    #         }
    #         QMessageBox QLabel {
    #             font-family: Arial, sans-serif;
    #             font-size: 14px;
    #             line-height: 1.6;
    #             color: #2c3e50;
    #         }
    #         QPushButton {
    #             background-color: #3498db;
    #             color: white;
    #             border: none;
    #             border-radius: 5px;
    #             padding: 8px;
    #             margin: 5px;
    #         }
    #         QPushButton:hover {
    #             background-color: #2980b9;
    #         }
    #         QPushButton:pressed {
    #             background-color: #1d6fa5;
    #         }
    #     """)

    #     help_box.exec()

    def show_main_window(self):
        """显示主窗口"""
        self.main_window.show()
        self.main_window.raise_()
        self.main_window.activateWindow()

    def quit_application(self):
        """退出应用程序"""
        QApplication.quit()

    def on_tray_icon_activated(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            self.show_main_window()
