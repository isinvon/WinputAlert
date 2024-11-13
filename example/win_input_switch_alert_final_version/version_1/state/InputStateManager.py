class InputStateManager:
    """ 
    输入法全局状态管理
    """
    def __init__(self):
        self._input_status = ""

    def set_status(self, status):
        """ 
        设置输入法状态
        """
        self._input_status = status
        print(f"Input status set to: {status}")

    def get_status(self):
        """ 
        获取输入法状态
        """
        print(f"Input status get: {self._input_status}")
        return self._input_status
    


# 全局状态管理实例
# state_manager = StateManager()
