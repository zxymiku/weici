import pygetwindow as gw
import pyautogui
import pytesseract
from PIL import Image

window_title = "test.txt - Notepad"
window = gw.getWindowsWithTitle(window_title)[0]

if window.isMinimized:
    window.restore()

window.activate()

left, top, width, height = window.left, window.top, window.width, window.height

window_left = -818
window_top = 263
window_width = 900
window_height = 900

screenshot = pyautogui.screenshot(region=(left + window_left, top + window_top, window_width, window_height))

screenshot.save('window_screenshot.png')

image = Image.open('window_screenshot.png')

text = pytesseract.image_to_string(image, lang='eng')  # lang参数指定英文

print(text)
