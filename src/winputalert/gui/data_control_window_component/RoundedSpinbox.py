from PySide6.QtWidgets import QSpinBox


class RoundedSpinBox(QSpinBox):
    """
    自定义圆角样式的 SpinBox。
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowOpacity(0.2)
        self.setStyleSheet("""
            QSpinBox {
                background-color: white;
                border: 1px solid #ced4da;
                border-radius: 8px; /* 圆角样式 */
                padding: 4px;
                font-size: 14px;
            }
            QSpinBox::up-button, QSpinBox::down-button {
                width: 16px;
                border: none;
                background-color: #cad6db;
                border-radius: 4px;
            }
            QSpinBox::up-button:hover, QSpinBox::down-button:hover {
                background-color: #606669;
            }
            QSpinBox::up-arrow {
                border: none;
                color: black; /* 上箭头颜色 */
                subcontrol-origin: padding;
                subcontrol-position: center;
                width: 10px;
                height: 10px;
            }
            QSpinBox::down-arrow {
                border: none;
                color: black; /* 下箭头颜色 */
                subcontrol-origin: padding;
                subcontrol-position: center;
                width: 10px;
                height: 10px;
            }
        """)
