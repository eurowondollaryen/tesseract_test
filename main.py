import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

import fitz #for pdf
doc = fitz.open('test.pdf')
page = doc.load_page(0)
mat = fitz.Matrix(4,4)
pix = page.get_pixmap(matrix = mat)
output = 'test.png'
pix.save(output)

a = Image.open('test.png')
result = pytesseract.image_to_string(a, lang='kor')
print(result)
#a = Image.open('영수증.jpg')
#result = pytesseract.image_to_string(a)
#print(result)
