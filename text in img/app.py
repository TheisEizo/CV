#%% IMPORT AND SETUP
import pdf2image as p2i
import os
import PIL
import pytesseract

pytesseract.pytesseract.tesseract_cmd = (
    r'C:\Users\45414\AppData\Local\Tesseract-OCR\tesseract')

name = 'test'

#%% CONVERT PDF PAGES TO PNG FILES IN FOLDER
first = 0 #page
last   = 9 #page

pages = p2i.convert_from_path(f'{name}.pdf',
                              first_page=first, last_page=last)

if f'{name}' not in os.listdir():
    os.mkdir(f'{name}')

if not first: first = 0
for n, page in enumerate(pages):
    page.save(f'{name}/{name}_{n+first}.png', 'png')
    
#%% EXCTRAT TEXT FROM PNG
output = {}
for path in os.listdir(f'{name}'):
    img = PIL.Image.open(f'{name}/{path}').convert("RGB")
    output[path.split('.')[0].split('_')[1]] = (
        pytesseract.image_to_string(img, lang='dan'))
   