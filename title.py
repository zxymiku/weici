from pywinauto import Desktop
all_windows = Desktop(backend="uia").windows()
for win in all_windows:
    print(win.window_text())
