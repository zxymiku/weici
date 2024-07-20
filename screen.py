import pygetwindow as gw
import pyautogui

# 获取特定窗口的句柄
window_title = "MuMu模拟器12"  # 替换为您的窗口标题
window = gw.getWindowsWithTitle(window_title)[0]

# 确保窗口是可见的
if window.isMinimized:
    window.restore()

# 获取窗口的位置和大小
window_x, window_y, window_width, window_height = window.left, window.top, window.width, window.height

# 定义相对窗口的坐标和截图的大小
relative_x = 10  # 相对于窗口左边缘的X坐标
relative_y = 200  # 相对于窗口上边缘的Y坐标
relative_width = 200  # 截图的宽度
relative_height = 60  # 截图的高度

# 计算实际的屏幕坐标
screen_x = window_x + relative_x
screen_y = window_y + relative_y

# 捕获屏幕截图
screenshot = pyautogui.screenshot(region=(screen_x, screen_y, relative_width, relative_height))

# 保存截图到文件
screenshot.save('screenshot.png')

print('Screenshot saved as screenshot.png')
