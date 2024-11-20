from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QWidget


class WindowRestartTool:
    @staticmethod
    def restart_window(window: QWidget, on_restart_complete: callable = None):
        """
        关闭当前窗口并重新启动它
        :param window: 要重启的窗口实例
        :param on_restart_complete: 回调函数，当重启完成后执行
        """
        if window.isVisible():
            window.close()  # 关闭窗口

        # 确保窗口对象被销毁
        window.deleteLater()
        QApplication.processEvents()  # 强制刷新事件循环

        # 等待销毁完成后创建新的实例
        def recreate_window():
            new_window = type(window)()  # 动态创建窗口实例
            new_window.show()  # 显示新的窗口
            if on_restart_complete:
                on_restart_complete(new_window)

        QTimer.singleShot(50, recreate_window)  # 延迟执行以确保销毁完成
