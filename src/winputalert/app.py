"""
WinputAlert 是一款基于 Python 开发的输入法状态切换提示的GUI应用
"""

import importlib.metadata
import sys

from PySide6 import QtWidgets

from winputalert.listener.StatusListener import StatusListener
from winputalert.system_tray.SystemTray import SystemTray


class WinputAlert(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.w_input_alert_ui()

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
    # 输入法状态提示界面
    main_window = WinputAlert()
    # 系统托盘
    tray = SystemTray()
    sys.exit(app.exec())
