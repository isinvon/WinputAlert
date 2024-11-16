# # 成功环境：win10 64位，搜狗输入法,win11 64位 微信输入法
# # 需要安装 pypywin32 库
# # 不要使用code runner插件运行，不然会打印出找不到win32Api模块
# 此工具类参考
# 1️⃣：https://www.tndyx.cc/docs/%E7%A8%8B%E5%BA%8F%E4%BB%A3%E7%A0%81/python/2024-04-06python%E4%B8%AD%E8%8B%B1%E6%96%87%E8%BE%93%E5%85%A5%E6%B3%95%E5%88%87%E6%8D%A2/
# 2️⃣：https://www.bilibili.com/opus/922363184816324644

import win32api
import win32con
import win32gui
import time
import ctypes

from enums.InputStatusCode import InputStatusCode
from state.InputStateManager import InputStateManager


class InputInfoUtil:
    """ 
    输入法工具类

    方法：

    switch_input_status: 切换输入法状态
    """

    def __init__(self):
        self.IMC_GETOPENSTATUS = 0x0005
        self.IMC_SETOPENSTATUS = 0x0006
        self.imm32 = ctypes.WinDLL('imm32', use_last_error=True)

    def switch_input_status(self):

        handle = win32gui.GetForegroundWindow()  # 某进程窗口句柄
        # bug修复：改为使用self.imm32
        hIME = self.imm32.ImmGetDefaultIMEWnd(handle)

        status = win32api.SendMessage(
            hIME, win32con.WM_IME_CONTROL, self.IMC_GETOPENSTATUS, 0)  # 返回值 0:英文 1:中文

        # 判断大小写是否开启
        is_caps_lock_on = ctypes.windll.user32.GetKeyState(0x14) & 0x0001

        # 判断当前输入法状态
        if status:
            InputStateManager.set_status(
                InputStatusCode.CHINESE.value)  # 设置为中文
            # print('当前中文，切换为英文') # debug
            # win32api.SendMessage(hIME, win32con.WM_IME_CONTROL, self.IMC_SETOPENSTATUS, 0)  # 关闭中文
        else:
            InputStateManager.set_status(
                InputStatusCode.ENGLISH.value)  # 设置为英文
            # print('当前英文，切换为中文') # debug
            # win32api.SendMessage(hIME, win32con.WM_IME_CONTROL, self.IMC_SETOPENSTATUS, 1)  # 开启中文

        # 输出大小写状态
        if is_caps_lock_on:
            InputStateManager.set_status(
                InputStatusCode.UPPERCASE.value)  # 设置为大写
            # print('Caps Lock已开启') # debug
        else:
            InputStateManager.set_status(
                InputStatusCode.LOWERCASE.value)  # 设置为小写
            # print('Caps Lock未开启') # debug

    
    def get_input_status(self):
        """ 
        获取输入法状态
        
        返回值：
        - InputStatusCode.CHINESE.value: 中文
        - InputStatusCode.ENGLISH.value: 英文
        - InputStatusCode.UPPERCASE.value: 大写
        - InputStatusCode.LOWERCASE.value: 小写
        """
        # 输入法全局状态管理
        input_global_state = InputStateManager()

        handle = win32gui.GetForegroundWindow()  # 某进程窗口句柄
        # bug修复：改为使用self.imm32
        hIME = self.imm32.ImmGetDefaultIMEWnd(handle)

        status = win32api.SendMessage(
            hIME, win32con.WM_IME_CONTROL, self.IMC_GETOPENSTATUS, 0)  # 返回值 0:英文 1:中文

        # 判断大小写是否开启
        is_caps_lock_on = ctypes.windll.user32.GetKeyState(0x14) & 0x0001

        # 判断当前输入法状态
        if status:
            input_global_state.set_status(
                InputStatusCode.CHINESE.value)  # 设置为中文
        else:
            input_global_state.set_status(
                InputStatusCode.ENGLISH.value)  # 设置为英文

        # 输出大小写状态
        if is_caps_lock_on:
            input_global_state.set_status(
                InputStatusCode.UPPERCASE.value)  # 设置为大写
        else:
            input_global_state.set_status(
                InputStatusCode.LOWERCASE.value)  # 设置为小写

        return input_global_state.get_status()


# def switch_input_method():
#     IMC_GETOPENSTATUS = 0x0005
#     IMC_SETOPENSTATUS = 0x0006

#     imm32 = ctypes.WinDLL('imm32', use_last_error=True)
#     handle = win32gui.GetForegroundWindow()  # 某进程窗口句柄
#     hIME = imm32.ImmGetDefaultIMEWnd(handle)
#     status = win32api.SendMessage(
#         hIME, win32con.WM_IME_CONTROL, IMC_GETOPENSTATUS, 0)  # 返回值 0:英文 1:中文

#     # 判断大小写是否开启
#     is_caps_lock_on = ctypes.windll.user32.GetKeyState(0x14) & 0x0001

#     # 判断当前输入法状态
#     if status:
#         print('当前中文，切换为英文')
#         win32api.SendMessage(hIME, win32con.WM_IME_CONTROL,
#                              IMC_SETOPENSTATUS, 0)  # 关闭中文
#     else:
#         print('当前英文，切换为中文')
#         win32api.SendMessage(hIME, win32con.WM_IME_CONTROL,
#                              IMC_SETOPENSTATUS, 1)  # 开启中文

#     # 输出大小写状态
#     if is_caps_lock_on:
#         print('Caps Lock已开启')
#     else:
#         print('Caps Lock未开启')


# if __name__ == "__main__":
#     switch_input_method()