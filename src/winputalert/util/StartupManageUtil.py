import os
import sys
import winreg


class StartupManageUtil:
    """
    Windows 管理应用程序的开机启动设置的工具类。

    原理: 修改注册表

    注意:

    - (HKEY_CURRENT_USER 仅限于当前用户的设置，而 HKEY_LOCAL_MACHINE 则影响所有用户（需要管理员权限）)

    - 当不传入 app_name 时，工具会自动使用当前运行的 .exe 文件路径(仅仅在打包成exe之后)。

    - 当传入 app_name 时，工具会自动使用传入的app_name作为应用名称。一般是 C:/Users/你的用户名/app_name.exe
    """

    @staticmethod
    def set_startup(enable: bool, app_name: str = None, system_wide: bool = False):
        """
        设置或取消应用程序的开机启动。



        :param enable: 是否启用开机启动 (True/False)
        :param app_name: 程序名称
        :param system_wide: 是否修改系统级的开机启动项，默认为 False (即仅修改当前用户的启动项)

        注意:

        - 普通软件自启动只需要用户层级即可(即默认的system_wide 为 False即可)

        - 当不传入 app_name 时，工具会自动使用当前运行的 .exe 文件路径(仅仅在打包成exe之后)。

        - 当传入 app_name 时，工具会自动使用传入的app_name作为应用名称。
        """
        # 如果是打包后的exe程序，则app_name为None，使用当前执行文件路径
        if app_name is None:
            app_path = sys.executable  # 获取当前exe文件的路径
            app_name = os.path.basename(app_path)  # 提取文件名作为应用名称
        else:
            app_path = os.path.join(os.getcwd(), f"{app_name}.exe")  # 获取应用程序路径

        reg_path = r"Software\Microsoft\Windows\CurrentVersion\Run" if not system_wide else r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"

        try:
            # 根据 system_wide 参数选择打开对应的注册表键
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER if not system_wide else winreg.HKEY_LOCAL_MACHINE,
                                 reg_path, 0, winreg.KEY_WRITE)

            if enable:
                # 设置开机启动项
                winreg.SetValueEx(key, app_name, 0,
                                  winreg.REG_SZ, app_path)
                print(f"{app_name} 已设置为开机启动.")
            else:
                # 取消开机启动项
                try:
                    winreg.DeleteValue(key, app_name)
                    print(f"{app_name} 已取消开机启动.")
                except FileNotFoundError:
                    print(f"{app_name} 未设置为开机启动.")

            # 关闭注册表键
            winreg.CloseKey(key)

        except Exception as e:
            print(f"操作失败: {e}")

    @staticmethod
    def is_startup_enabled(app_name: str = None, system_wide: bool = False) -> bool:
        """
        检查应用程序是否已设置为开机启动。

        :param app_name: 程序名称
        :param system_wide: 是否检查系统级的开机启动项，默认为 False (即仅检查当前用户的启动项)
        :return bool: 如果应用程序设置为开机启动，返回 True 否则返回 False。

        注意:

        - 普通软件自启动只需要用户层级即可(即默认的system_wide 为 False即可)

        - 当不传入 app_name 时，工具会自动使用当前运行的 .exe 文件路径(仅仅在打包成exe之后)。

        - 当传入 app_name 时，工具会自动使用传入的app_name作为应用名称。
        """

        # 如果是打包后的exe程序，则app_name为None，使用当前执行文件路径
        if app_name is None:
            app_path = sys.executable  # 获取当前exe文件的路径
            app_name = os.path.basename(app_path)  # 提取文件名作为应用名称
        else:
            app_path = os.path.join(os.getcwd(), f"{app_name}.exe")  # 获取应用程序路径

        reg_path = r"Software\Microsoft\Windows\CurrentVersion\Run" if not system_wide else r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"

        try:
            # 根据 system_wide 参数选择打开对应的注册表键
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER if not system_wide else winreg.HKEY_LOCAL_MACHINE,
                                 reg_path, 0, winreg.KEY_READ)
            try:
                # 读取注册表中是否存在该应用的启动项
                winreg.QueryValueEx(key, app_name)
                winreg.CloseKey(key)
                return True  # 如果存在该项，说明已设置为开机启动
            except FileNotFoundError:
                winreg.CloseKey(key)
                return False  # 如果未找到该项，说明未设置为开机启动
        except Exception as e:
            print(f"读取注册表失败: {e}")
            return False  # 如果读取失败，返回 False


# 使用示例
# if __name__ == "__main__":

#     app_name = "doubao"

#     # ==============用户层级测试(普通软件自启动只需要用户层级即可)=================

#     # 检查是否启用了当前用户的开机启动
#     if StartupManageUtil.is_startup_enabled(app_name=app_name):
#         print(f"{app_name} 已启用当前用户开机启动.")
#     else:
#         print(f"{app_name} 未启用当前用户开机启动.")

#     # 设置当前用户的开机启动
#     StartupManageUtil.set_startup(enable=True, app_name=app_name, system_wide=False)

#     # 取消当前用户的开机启动
#     StartupManageUtil.set_startup(enable=False, app_name=app_name, system_wide=False)


#     # ==============系统层级测试=================

#     # # 检查是否启用了系统级的开机启动（需要管理员权限）
#     if StartupManageUtil.is_startup_enabled(app_name=app_name, system_wide=True):
#         print(f"{app_name} 已启用系统级开机启动.")
#     else:
#         print(f"{app_name} 未启用系统级开机启动.")

#     # # 设置系统级的开机启动（需要管理员权限）
#     StartupManageUtil.set_startup(enable=True, app_name=app_name, system_wide=True)

#     # # 取消系统级的开机启动（需要管理员权限）
#     StartupManageUtil.set_startup(enable=False, app_name=app_name, system_wide=True)
