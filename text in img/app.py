#%% IMPORT AND SETUP
import pdf2image as p2i
import os
import PIL
import pytesseract
from PyPDF2 import PdfFileMerger

pytesseract.pytesseract.tesseract_cmd = (
    r'C:\Users\45414\AppData\Local\Tesseract-OCR\tesseract')

name = 'test'

#%% CONVERT PDF PAGES TO PNG FILES IN FOLDER
if f'{name}' not in os.listdir():
    os.mkdir(f'{name}')

first = 0 #page
last   = 9 #page

pages = p2i.convert_from_path(f'{name}.pdf',
                              first_page=first, last_page=last)

if not first: first = 0
for n, page in enumerate(pages):
    page.save(f'{name}/{name}_{n+first}.png', 'png')
    
#%% EXCTRAT TEXT TO PYTHON FROM PNG
output = {}
for path in os.listdir(f'{name}'):
    img = PIL.Image.open(f'{name}/{path}').convert("RGB")
    key_name = path.split('.')[0].split('_')[1]
    output[key_name] = (
        pytesseract.image_to_string(img, lang='dan'))

#%% MAKE PNG FILES TO OCR PDFS
for path in os.listdir(f'{name}'):
    pdf = pytesseract.image_to_pdf_or_hocr(f'{name}/{path}', extension='pdf')
    pdf_name = f'{name}/{path}'.split('.')[0]
    with open(pdf_name+'.pdf', 'w+b') as f:
        f.write(pdf)

#%%  MAKE COMBINE ALL OCR PDFS INTO ONE OCR PDF
pdf_merger = PdfFileMerger()
for path in os.listdir(f'{name}'):
    if path.split('.')[-1] == 'pdf':
        pdf_merger.append(f'{name}/{path}')
pdf_merger.write(f'{name}_ocr.pdf')
