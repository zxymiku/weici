import pytesseract
from PIL import Image
pytesseract.tesseract_cmd = r'D:\Tesseract-OCR\tesseract.exe'
img = Image.open('screenshot.png')
subject = pytesseract.image_to_string(img,lang='chi_sim+eng')

