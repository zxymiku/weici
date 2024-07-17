from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract-OCR\tesseract.exe'
image = Image.open(r'C:\Users\Divin\Desktop\weici\test.png')
text = pytesseract.image_to_string(image, lang='eng')
print(text)
