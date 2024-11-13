from enum import Enum

class InputStatusCode(Enum):
    """
    输入法状态
    """
    CHINESE = 1
    """ 
    中文 1
    """
    ENGLISH = 2
    """ 
    英文 2
    """
    UPPERCASE = 3
    """
    大写 3
    """
    LOWERCASE = 4
    """
    小写 4
    """
    
# 获取值的方式 
# input_status_code = InputStatusCode.CHINESE.value
# 获取键的方式
# input_status_code = InputStatusCode.CHINESE.name