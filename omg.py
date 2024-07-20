import pytesseract
from PIL import Image

# 指定Tesseract可执行文件的位置，如果不在系统路径中
pytesseract.tesseract_cmd = r'D:\Tesseract-OCR\tesseract.exe'

# 打开图片文件
img = Image.open('screenshot.png')

config = ('-l chi_sim --oem 1 --psm 3')

# 使用Tesseract进行OCR识别
text = pytesseract.image_to_string(img,config=config)

print(text)
