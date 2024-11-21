"""
WinputAlert 是一款基于 Python 开发的输入法状态切换提示的GUI应用
"""

import importlib.metadata
import sys

from PySide6 import QtWidgets

from winputalert.config.SystemConfig import SystemConfig
from winputalert.gui.DataControlWindow import DataControlWindow
from winputalert.listener.StatusListener import StatusListener
from winputalert.system_tray.SystemTray import SystemTray
from winputalert.util.StartupManageUtil import StartupManageUtil


class WinputAlert(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.w_input_alert_ui()        

        # 创建 DataControlWindow 实例
        self.data_control_window = DataControlWindow()

        # 创建系统托盘实例
        self.tray = SystemTray()

        # 连接信号：当托盘图标点击时，显示 DataControlWindow
        self.tray.show_data_control_window_signal.connect(self.show_data_control_window)
        
        # 对第一次启动进行开机启动判断
        system_config = SystemConfig()
        if system_config.get_auto_start_on_system_boot():
            if not StartupManageUtil.is_startup_enabled(system_wide=False):
                StartupManageUtil.set_startup(enable=True,system_wide=False)
        else:
            StartupManageUtil.set_startup(enable=False,system_wide=False)
            
    # def show_data_control_window(self):
    #     """显示 DataControlWindow"""
    #     self.data_control_window.show()
    
    def show_data_control_window(self):
        """显示或重新创建 DataControlWindow"""
        if not hasattr(self, 'data_control_window') or self.data_control_window is None:
            self.data_control_window = DataControlWindow()  # 重新创建窗口
        self.data_control_window.show()
        self.data_control_window.destroyed.connect(self.on_data_control_window_destroyed)
    
    def on_data_control_window_destroyed(self):
        """窗口销毁时清理引用"""
        self.data_control_window = None
        
    def w_input_alert_ui(self):
        listener = StatusListener()
        # 启动输入法监听
        listener.start_listening()


def main():
    # Linux desktop environments use an app's .desktop file to integrate the app
    # in to their application menus. The .desktop file of this app will include
    # the StartupWMClass key, set to app's formal name. This helps associate the
    # app's windows to its menu item.
    #
    # For association to work, any windows of the app must have WMCLASS property
    # set to match the value set in app's desktop file. For PySide6, this is set
    # with setApplicationName().

    # Find the name of the module that was used to start the app
    app_module = sys.modules["__main__"].__package__
    # Retrieve the app's metadata
    metadata = importlib.metadata.metadata(app_module)
    QtWidgets.QApplication.setApplicationName(metadata["Formal-Name"])
    app = QtWidgets.QApplication(sys.argv)
    # 确保关闭最后一个窗口时应用不会退出
    app.setQuitOnLastWindowClosed(False)
    # 输入法状态提示界面
    main_window = WinputAlert()
    # system_config = SystemConfig()
    # system_config.set_auto_start_on_system_boot(False)
    # print("=====================")
    # print(system_config.get_auto_start_on_system_boot())
    # print(type(system_config.get_auto_start_on_system_boot()))
    sys.exit(app.exec())
