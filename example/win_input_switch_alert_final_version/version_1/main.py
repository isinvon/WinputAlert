import ctypes
import sys
import time

import win32api
import win32con
import win32gui
from PyQt5.QtCore import QTimer
# 解决无法从源解析导入“PyQt5.QtWidgets”的问题，参考： https://blog.csdn.net/qq_39938666/article/details/121895038
from PyQt5.QtWidgets import QApplication

from gui.ChineseWindow import ChineseWindow
from gui.EnglishWindow import EnglishWindow
from gui.LowerCaseWindow import LowerCaseWindow
from gui.UpperCaseWindow import UpperCaseWindow

# def switch_input_method():
#     IMC_GETOPENSTATUS = 0x0005
#     imm32 = ctypes.WinDLL('imm32', use_last_error=True)
#     handle = win32gui.GetForegroundWindow()
#     hIME = imm32.ImmGetDefaultIMEWnd(handle)
#     status = win32api.SendMessage(hIME, win32con.WM_IME_CONTROL, IMC_GETOPENSTATUS, 0)

#     is_caps_lock_on = ctypes.windll.user32.GetKeyState(0x14) & 0x0001

#     if status:
#         ChineseWindow()
#         print('当前中文')
#     else:
#         EnglishWindow()
#         print('当前英文')

#     if is_caps_lock_on:
#         UpperCaseWindow()
#         print('Caps Lock已开启')
#     else:
#         LowerCaseWindow()
#         print('Caps Lock未开启')

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     switch_input_method()
#     sys.exit(app.exec_()) # 启动应用程序
            # main.py




# class StatusListener:
#     def __init__(self):
#         self.current_input_method = None
#         self.current_caps_lock_state = None
#         self.timer = QTimer()
#         self.timer.timeout.connect(self.check_status)
#         self.timer.start(500)  # 每500毫秒检查一次状态

#         self.hide_timer = QTimer()
#         self.hide_timer.setSingleShot(True)  # 设置为单次触发

#         self.window = None  # 存储当前显示的窗口

#     def check_status(self):
#         IMC_GETOPENSTATUS = 0x0005
#         imm32 = ctypes.WinDLL('imm32', use_last_error=True)
#         handle = win32gui.GetForegroundWindow()
#         hIME = imm32.ImmGetDefaultIMEWnd(handle)
#         input_method_status = win32api.SendMessage(hIME, win32con.WM_IME_CONTROL, IMC_GETOPENSTATUS, 0)
        
#         caps_lock_state = ctypes.windll.user32.GetKeyState(0x14) & 0x0001

#         # 检查输入法状态是否变化
#         if input_method_status != self.current_input_method:
#             self.current_input_method = input_method_status
#             self.show_input_method_window()

#         # 检查Caps Lock状态是否变化
#         if caps_lock_state != self.current_caps_lock_state:
#             self.current_caps_lock_state = caps_lock_state
#             self.show_caps_lock_window()

#     def show_input_method_window(self):
#         if self.window:
#             self.window.close()
#         if self.current_input_method:
#             self.window = ChineseWindow()
#             print("当前中文输入法")
#         else:
#             self.window = EnglishWindow()
#             print("当前英文输入法")
#         self.window.show()
#         self.start_hide_timer()  # 启动隐藏计时器

#     def show_caps_lock_window(self):
#         if self.window:
#             self.window.close()
#         if self.current_caps_lock_state:
#             self.window = UpperCaseWindow()
#             print("Caps Lock已开启")
#         else:
#             self.window = LowerCaseWindow()
#             print("Caps Lock未开启")
#         self.window.show()
#         self.start_hide_timer()  # 启动隐藏计时器

#     def start_hide_timer(self):
#         self.hide_timer.timeout.connect(self.hide_window)  # 计时器触发时关闭窗口
#         self.hide_timer.start(500)  # 设置为两秒后自动隐藏

#     def hide_window(self):
#         if self.window:
#             self.window.close()
#             self.window = None  # 清除窗口引用

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     listener = StatusListener()  # 创建状态监听器
#     sys.exit(app.exec_())




# class StatusListener:
#     def __init__(self):
#         self.current_input_method = None
#         self.current_caps_lock_state = None

#         # 定时器用于检查状态变化
#         self.timer = QTimer()
#         self.timer.timeout.connect(self.check_status)
#         self.timer.start(500)  # 每500毫秒检查一次状态

#         # 定时器用于窗口自动隐藏
#         self.hide_timer = QTimer()
#         self.hide_timer.setSingleShot(True)

#         # 用于存储窗口并控制显示与隐藏
#         self.window = None  

#     def check_status(self):
#         IMC_GETOPENSTATUS = 0x0005
#         imm32 = ctypes.WinDLL('imm32', use_last_error=True)
#         handle = ctypes.windll.user32.GetForegroundWindow()
#         hIME = imm32.ImmGetDefaultIMEWnd(handle)
#         input_method_status = ctypes.windll.user32.SendMessageW(hIME, 0x0283, IMC_GETOPENSTATUS, 0)
        
#         caps_lock_state = ctypes.windll.user32.GetKeyState(0x14) & 0x0001

#         # 检查输入法状态是否变化
#         if input_method_status != self.current_input_method:
#             self.current_input_method = input_method_status
#             self.show_input_method_window()

#         # 检查Caps Lock状态是否变化
#         if caps_lock_state != self.current_caps_lock_state:
#             self.current_caps_lock_state = caps_lock_state
#             self.show_caps_lock_window()

#     def show_input_method_window(self):
#         if self.window is None:
#             self.window = ChineseWindow() if self.current_input_method else EnglishWindow()
#         else:
#             # 切换窗口内容而不关闭
#             self.window.hide()
#             if self.current_input_method:
#                 self.window = ChineseWindow()
#             else:
#                 self.window = EnglishWindow()
        
#         self.window.show()
#         self.start_hide_timer()  # 启动隐藏计时器

#     def show_caps_lock_window(self):
#         if self.window is None:
#             self.window = UpperCaseWindow() if self.current_caps_lock_state else LowerCaseWindow()
#         else:
#             # 切换窗口内容而不关闭
#             self.window.hide()
#             if self.current_caps_lock_state:
#                 self.window = UpperCaseWindow()
#             else:
#                 self.window = LowerCaseWindow()

#         self.window.show()
#         self.start_hide_timer()  # 启动隐藏计时器

#     def start_hide_timer(self):
#         self.hide_timer.timeout.connect(self.hide_window)
#         self.hide_timer.start(2000)  # 设置为两秒后自动隐藏

#     def hide_window(self):
#         if self.window:
#             self.window.hide()  # 表面上隐藏窗口，但不销毁

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     listener = StatusListener()  # 创建状态监听器
#     sys.exit(app.exec_())



class StatusListener:
    def __init__(self):
        self.current_input_method = None
        self.current_caps_lock_state = None

        # 定时器用于检查状态变化
        self.timer = QTimer()
        self.timer.timeout.connect(self.check_status)
        self.timer.start(1)  # 每1毫秒检查一次状态

        # 定时器用于窗口自动隐藏
        self.hide_timer = QTimer()
        self.hide_timer.setSingleShot(True)

        # 用于存储窗口并控制显示与隐藏
        self.window = None  

    def check_status(self):
        IMC_GETOPENSTATUS = 0x0005
        imm32 = ctypes.WinDLL('imm32', use_last_error=True)
        handle = ctypes.windll.user32.GetForegroundWindow()
        hIME = imm32.ImmGetDefaultIMEWnd(handle)
        input_method_status = ctypes.windll.user32.SendMessageW(hIME, 0x0283, IMC_GETOPENSTATUS, 0)
        
        caps_lock_state = ctypes.windll.user32.GetKeyState(0x14) & 0x0001

        # 检查输入法状态是否变化
        if input_method_status != self.current_input_method:
            self.current_input_method = input_method_status
            self.show_input_method_window()

        # 检查Caps Lock状态是否变化
        if caps_lock_state != self.current_caps_lock_state:
            self.current_caps_lock_state = caps_lock_state
            self.show_caps_lock_window()

    def show_input_method_window(self):
        if self.window is None:
            self.window = ChineseWindow() if self.current_input_method else EnglishWindow()
        else:
            # 仅隐藏当前窗口而不销毁
            self.window.hide()
            if self.current_input_method:
                self.window = ChineseWindow()  # 更新为中文输入法窗口
            else:
                self.window = EnglishWindow()  # 更新为英文输入法窗口
        
        self.window.show()  # 显示更新后的窗口
        self.start_hide_timer()  # 启动隐藏计时器

    def show_caps_lock_window(self):
        if self.window is None:
            self.window = UpperCaseWindow() if self.current_caps_lock_state else LowerCaseWindow()
        else:
            # 仅隐藏当前窗口而不销毁
            self.window.hide()
            if self.current_caps_lock_state:
                self.window = UpperCaseWindow()  # 更新为大写窗口
            else:
                self.window = LowerCaseWindow()  # 更新为小写窗口

        self.window.show()  # 显示更新后的窗口
        self.start_hide_timer()  # 启动隐藏计时器

    def start_hide_timer(self):
        self.hide_timer.timeout.connect(self.hide_window)
        self.hide_timer.start(1000)  # 设置为1秒后自动隐藏

    def hide_window(self):
        if self.window:
            self.window.hide()  # 表面上隐藏窗口，但不销毁

if __name__ == '__main__':
    app = QApplication(sys.argv)
    listener = StatusListener()  # 创建状态监听器
    sys.exit(app.exec_())