# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 14:00:15 2020

@author: Theis Eizo
"""

from wand.image import Image

with Image(filename='sample_doc.pdf') as img:

    print('width =', img.width)
    print('height =', img.height)
    print('pages = ', len(img.sequence))
    print('resolution = ', img.resolution)

with img.convert('png') as converted:
     converted.save(filename='sample_doc.png')

#%%
import PIL
import pytesseract

TESSDATA_PREFIX = r'C:\Users\45414\AppData\Local\Tesseract-OCR'

pytesseract.pytesseract.tesseract_cmd = TESSDATA_PREFIX+'\\tesseract'

img = PIL.Image.open('sample_doc.png').convert("RGB")
output = pytesseract.image_to_string(img, lang='dan')
print(output)
