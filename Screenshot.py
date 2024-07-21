import pygetwindow as gw
import pyautogui

window_title = "MuMu模拟器12"
window = gw.getWindowsWithTitle(window_title)[0]

if window.isMinimized:
    window.restore()

window_x, window_y, window_width, window_height = window.left, window.top, window.width, window.height
relative_x = 10
relative_y = 200
relative_width = 200
relative_height = 60
screen_x = window_x + relative_x
screen_y = window_y + relative_y
screenshot = pyautogui.screenshot(region=(screen_x, screen_y, relative_width, relative_height))
screenshot.save('screenshot.png')
print('Screenshot saved as screenshot.png')
