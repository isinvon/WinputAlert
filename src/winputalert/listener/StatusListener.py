import ctypes

import keyboard
from PySide6.QtCore import QEvent, QObject, QTimer
from PySide6.QtWidgets import QApplication

from winputalert.config.GUIConfig import GUIConfig
from winputalert.config.KeyboardConfig import KeyboardConfig
from winputalert.gui.transparent_window_children.ChineseWindow import ChineseWindow
from winputalert.gui.transparent_window_children.EnglishWindow import EnglishWindow
from winputalert.gui.transparent_window_children.LowerCaseWindow import LowerCaseWindow
from winputalert.gui.transparent_window_children.UpperCaseWindow import UpperCaseWindow


class StatusListener(QObject):
    """ 
    状态监听器

    已具备配置热更新特性，无需重启即可生效
    """

    def __init__(self):
        super().__init__()

        keyboard_config = KeyboardConfig()

        self.current_input_method = None
        self.current_caps_lock_state = None
        self.window = None

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_status)
        self.timer.setInterval(
            keyboard_config.get_keyboard_detect_time_interval())  # 每隔 1 毫秒检查一次

        self.hide_timer = None
        self.is_listening = False
        self.listen_thread = None

    def start_listening(self):
        if not self.is_listening:
            keyboard.hook(self.on_key_press)
            self.is_listening = True

    def stop_listening(self):
        if self.is_listening:
            keyboard.unhook_all()
            self.is_listening = False

    def on_key_press(self, event):
        if event.name in {"shift", "caps lock"}:
            if not self.timer.isActive():
                QApplication.postEvent(self, QEvent(QEvent.Type.User))
        if event.name == "ctrl" and keyboard.is_pressed("space"):
            if not self.timer.isActive():
                QApplication.postEvent(self, QEvent(QEvent.Type.User))

    def customEvent(self, event):
        self.timer.start()

    def check_status(self):
        IMC_GETOPENSTATUS = 0x0005
        imm32 = ctypes.WinDLL('imm32', use_last_error=True)
        handle = ctypes.windll.user32.GetForegroundWindow()
        hIME = imm32.ImmGetDefaultIMEWnd(handle)
        input_method_status = ctypes.windll.user32.SendMessageW(
            hIME, 0x0283, IMC_GETOPENSTATUS, 0)

        caps_lock_state = ctypes.windll.user32.GetKeyState(0x14) & 0x0001

        if input_method_status != self.current_input_method:
            self.current_input_method = input_method_status
            self.show_input_method_window()

        if caps_lock_state != self.current_caps_lock_state:
            self.current_caps_lock_state = caps_lock_state
            self.show_caps_lock_window()

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
        if self.hide_timer:
            self.hide_timer.stop()

        self.hide_timer = QTimer(self)
        self.hide_timer.setSingleShot(True)
        self.hide_timer.timeout.connect(self.hide_window)

        gui_config = GUIConfig()
        self.hide_timer.start(gui_config.get_gui_delay_close_time())

    def hide_window(self):
        if self.window:
            self.window.hide()
        self.hide_timer = None
        self.start_listening()
