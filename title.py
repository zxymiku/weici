from pywinauto import Desktop

# 获取所有顶层窗口的句柄和标题
all_windows = Desktop(backend="uia").windows()

# 遍历所有窗口并打印它们的标题
for win in all_windows:
    print(win.window_text())
