import pygetwindow as gw
import pyautogui
import pytesseract
from PIL import Image

window_title = "Target Window Title"
window = gw.getWindowsWithTitle(window_title)[0]

if window.isMinimized:
    window.restore()

window.activate()

left, top, width, height = window.left, window.top, window.width, window.height

window_left = 50
window_top = 50
window_width = 300
window_height = 200

screenshot = pyautogui.screenshot(region=(left + window_left, top + window_top, window_width, window_height))

screenshot.save('window_screenshot.png')

image = Image.open('window_screenshot.png')

text = pytesseract.image_to_string(image, lang='eng')  # lang参数指定英文

print(text)
