import pyautogui
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
import time

# 设置Tesseract-OCR的路径
pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract-OCR\tesseract.exe'  # 修改为您Tesseract-OCR的安装路径


def get_mouse_click_coordinates():
    print("请在5秒内点击区域的起始点...")
    time.sleep(5)
    start_x, start_y = pyautogui.position()
    print(f"起始点坐标: ({start_x}, {start_y})")

    print("请在2秒内点击区域的结束点...")
    time.sleep(2)
    end_x, end_y = pyautogui.position()
    print(f"结束点坐标: ({end_x}, {end_y})")

    return (start_x, start_y, end_x, end_y)


def capture_screenshot(start_x, start_y, end_x, end_y):
    left = min(start_x, end_x)
    top = min(start_y, end_y)
    right = max(start_x, end_x)
    bottom = max(start_y, end_y)
    width = right - left
    height = bottom - top

    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    screenshot.save('screenshot.png')
    return screenshot


def preprocess_image(image):
    # 转换为灰度图像
    gray_image = image.convert('L')
    # 增强对比度
    enhancer = ImageEnhance.Contrast(gray_image)
    enhanced_image = enhancer.enhance(2)
    # 应用二值化
    binary_image = enhanced_image.point(lambda p: p > 128 and 255)
    return binary_image


def perform_ocr(image):
    # 预处理图像
    preprocessed_image = preprocess_image(image)
    preprocessed_image.save('preprocessed_screenshot.png')
    text = pytesseract.image_to_string(preprocessed_image, lang='eng')  # 您可以选择适当的语言
    return text


if __name__ == "__main__":
    start_x, start_y, end_x, end_y = get_mouse_click_coordinates()
    screenshot = capture_screenshot(start_x, start_y, end_x, end_y)
    recognized_text = perform_ocr(screenshot)

    print("识别的文字如下：")
    print(recognized_text)
