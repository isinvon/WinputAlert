import tkinter as tk

def say_hello():
    label.config(text="Hello, Tkinter!")

root = tk.Tk()
root.title("Tkinter Demo")

# 设置窗口的透明度
root.attributes('-alpha', 0.1)

# 去掉窗口的标题栏和边框
root.overrideredirect(True)

# 设置窗口置顶
root.attributes('-topmost', True)

# 设置窗口宽度和高度
window_width = 120
window_height = 80

# 获取屏幕宽度和高度
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# 计算窗口左上角的x和y位置，使其水平居中并靠近顶部
x = (screen_width - window_width) // 2
y = screen_height // 80

# 设置窗口的宽高和位置
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# 设置标签和按钮的字体大小
label = tk.Label(root, text="中文", font=("Arial", 40))  # 字体大小30
label.pack(pady=10)

root.mainloop()
