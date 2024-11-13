
import ctypes
import sys

import keyboard  # 用于监听键盘事件
from gui.ChineseWindow import ChineseWindow
from gui.EnglishWindow import EnglishWindow
from gui.LowerCaseWindow import LowerCaseWindow
from gui.UpperCaseWindow import UpperCaseWindow
# 导入QTimer
from PyQt5.QtCore import QEvent, QObject, QTimer
from PyQt5.QtWidgets import QApplication


class StatusListener(QObject):
    def __init__(self):
        super().__init__()
        self.current_input_method = None
        self.current_caps_lock_state = None
        self.window = None

        # 定时器初始化为 None，定时器会在每次按下指定按键时启动
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_status)
        self.timer.setInterval(1)  # 每隔 1 毫秒检查一次

        # 用于隐藏窗口的定时器
        self.hide_timer = None
        # 监听标志
        self.is_listening = False  # 初始化为 False
        self.listen_thread = None

    def start_listening(self):
        if not self.is_listening:
            # 启动键盘钩子来监听所有按键事件
            keyboard.hook(self.on_key_press)
            self.is_listening = True
            # print("Started listening...") # debug

    def stop_listening(self):
        if self.is_listening:
            # 停止键盘钩子
            keyboard.unhook_all()
            self.is_listening = False
            # print("Stopped listening...") # debug

    def on_key_press(self, event):
        # 检测 Ctrl+Space 组合键
        if keyboard.is_pressed("ctrl") and event.name == "space":
            if not self.timer.isActive():
                QApplication.postEvent(self, QEvent(QEvent.User))

        # 检测 Shift 和 Caps Lock 键的独立状态
        elif event.name in {"shift", "caps lock", "left shift", "right shift"}:
            if not self.timer.isActive():
                QApplication.postEvent(self, QEvent(QEvent.User))

    def customEvent(self, event):
        # 在主线程中启动定时器，仅运行一次
        self.timer.start()

    def check_status(self):
        # 检查当前输入法状态
        IMC_GETOPENSTATUS = 0x0005
        imm32 = ctypes.WinDLL('imm32', use_last_error=True)
        handle = ctypes.windll.user32.GetForegroundWindow()
        hIME = imm32.ImmGetDefaultIMEWnd(handle)
        input_method_status = ctypes.windll.user32.SendMessageW(
            hIME, 0x0283, IMC_GETOPENSTATUS, 0)

        # 检查当前 Caps Lock 状态
        caps_lock_state = ctypes.windll.user32.GetKeyState(0x14) & 0x0001

        # 检查输入法状态是否变化
        if input_method_status != self.current_input_method:
            self.current_input_method = input_method_status
            self.show_input_method_window()

        # 检查 Caps Lock 状态是否变化
        if caps_lock_state != self.current_caps_lock_state:
            self.current_caps_lock_state = caps_lock_state
            self.show_caps_lock_window()

        # 状态检查完毕后停止定时器
        self.timer.stop()

    def show_input_method_window(self):
        if self.window is None:
            self.window = ChineseWindow() if self.current_input_method else EnglishWindow()
        else:
            self.window.hide()
            self.window = ChineseWindow() if self.current_input_method else EnglishWindow()

        self.window.show()
        self.start_hide_timer()

    def show_caps_lock_window(self):
        if self.window is None:
            self.window = UpperCaseWindow() if self.current_caps_lock_state else LowerCaseWindow()
        else:
            self.window.hide()
            self.window = UpperCaseWindow() if self.current_caps_lock_state else LowerCaseWindow()

        self.window.show()
        self.start_hide_timer()

    def start_hide_timer(self):
        # 如果隐藏定时器已经存在且正在计时，则重置定时器
        if self.hide_timer:
            self.hide_timer.stop()

        # 重新启动单次定时器，在 2 秒后隐藏窗口
        self.hide_timer = QTimer(self)
        self.hide_timer.setSingleShot(True)  # 单次触发
        self.hide_timer.timeout.connect(self.hide_window)
        self.hide_timer.start(2000)  # 2 秒后触发 hide_window

    def hide_window(self):
        if self.window:
            self.window.hide()
        self.hide_timer = None  # 重置隐藏定时器
        self.start_listening()  # 重新开始监听按键


if __name__ == '__main__':
    app = QApplication(sys.argv)

    listener = StatusListener()
    listener.start_listening()

    sys.exit(app.exec_())


# 解决的问题：

# 1️⃣如何解决按下其他按键的时候也会显示gui呢？
# 1. 仅在特定按键时启动一次定时器：我们可以增加条件判断，确保定时器仅在指定的按键（Shift 或 Caps Lock）按下后启动一次，并在定时器完成检测后停止。
# 2. 监听前台窗口的变更：通过增加逻辑来判断前台窗口变更时，是否真正需要重新检测状态，减少不必要的检测。


# 2️⃣如何实现如果连续按下，重新计时再执行hide_window？
# 1. 调整 start_hide_timer 方法的逻辑，使其在检测到新的按键事件时停止当前计时器并重新开始计时。这确保了每次按键后窗口保持可见 2 秒，而不会因为多次按键而立即隐藏。
# 2. start_hide_timer 每次按键触发时都会重新启动隐藏计时器，使窗口持续显示 2 秒。, 使用 setSingleShot(True) 确保计时器仅执行一次，并在超时后调用 hide_window。, hide_window 方法在隐藏窗口后将 hide_timer 重置为 None，为下一次按键做好准备。

# 3️⃣如何实现按下其他按键的时候也会显示gui呢？
""" 
# 关键代码
# 不要漏了左右shift的判断
def on_key_press(self, event):    
        # 检测 Ctrl+Space 组合键
        if keyboard.is_pressed("ctrl") and event.name == "space":
            if not self.timer.isActive():
                QApplication.postEvent(self, QEvent(QEvent.User))

        # 检测 Shift 和 Caps Lock 键的独立状态
        elif event.name in {"shift", "caps lock", "left shift", "right shift"}:
            if not self.timer.isActive():
                QApplication.postEvent(self, QEvent(QEvent.User))

"""
