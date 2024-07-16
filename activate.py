import pyautogui
import time
time.sleep(3)
x, y = pyautogui.position()
click_x, click_y = pyautogui.position()
relative_x = click_x - x
relative_y = click_y - y

print(f"点击位置相对于窗口的坐标是: ({relative_x}, {relative_y})")
