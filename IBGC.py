from lib2to3.pgen2.token import RPAR
from turtle import width
from urllib.parse import SplitResult
from pikepdf import Pdf
import os
import PyPDF2
import sys
import subprocess
import ocrmypdf
import pytesseract
import re
from pdf2image import convert_from_path
from PIL import Image
import argparse
import numpy as np
import cv2
import tempfile

def stitch(file, filename):
    # ext = [files for files in (file)]
    imgs = [Image.open(i) for i in file]
    # print(f'img {imgs} type: {type(imgs)}')
    min_img_width = min(i.width for i in imgs)

    total_height = 0
    for i, img in enumerate(imgs):
        if img.width > min_img_width:
            imgs[i] = img.resize(
                (min_img_width, int(img.height / img.width * min_img_width)), Image.ANTIALIAS)
        total_height += imgs[i].height

    new_img = Image.new(imgs[0].mode, (min_img_width, total_height))
    y = 0
    for img in imgs:
        new_img.paste(img, (0, y))
        y += img.height
    new_img.save(
        f'/home/caypro/Documents/ibgc/IBGC_PDF/{str(filename).split(".")[0]}.jpeg')

# stitch('/home/caypro/Documents/ibgc/IBGC_PDF/IBGC_PDF/jpeg')

def convert_to_jpeg(file):
    for root, dirs, files in os.walk(file):
        for name in files:
            if name.endswith('.pdf'):
                subprocess.run(["qpdf", "--replace-input", file + '/' + name])
                convert_to_jpeg(file + '/' + name)
    temp = []
    for root, dirs, files in os.walk(file):
        for name in files:
            with tempfile.TemporaryDirectory() as temp_dir:
                if name.endswith('.pdf'):
                    pages = convert_from_path(
                        file+'/'+name, output_folder=temp_dir)
                    # print(temp_dir)
                    for page_no in range(len(pages)):
                        image_path = f'{temp_dir}/{page_no}.png'
                        width, height = pages[page_no].size
                        pages[page_no].crop(
                            (0, 80, width-190, height-80)).save(image_path, 'PNG')
                        temp.append(image_path)
                    # print(temp)
                    stitch(temp, name)
                    temp.clear()

# convert_to_jpeg('/home/caypro/Documents/ibgc/IBGC_PDF/IBGC_PDF')

def repair(file):

    for root, dirs, files in os.walk(file):
        for name in files:
            if name.endswith('.pdf'):
                subprocess.run(["qpdf", "--replace-input", file + '/' + name])
                convert_to_jpeg(file + '/' + name)
# repair('/home/caypro/Documents/ibgc/IBGC_PDF/test')
def test(file):

    with Image.open(file) as im:

        width, height = im.size


    # Here the image "im" is cropped and assigned to new variable im_crop
        im_crop = im.crop((0, 80, width-190, height-80)).save('/home/caypro/Documents/Abhijeet/ibgc/IBGC_PDF/IBGC_PDF/jpeg/output.jpeg')
test ('/home/caypro/Documents/Abhijeet/ibgc/IBGC_PDF/IBGC_PDF/jpeg/0.jpeg')
# ocrmypdf.ocr('/home/caypro/Documents/Abhijeet/ibgc/IBGC_PDF/IBGC_0.jpeg', )

# 98,25,1491,2123
# img = cv2.imread('/home/caypro/Documents/ibgc/IBGC_PDF/IBGC_PDF/jpeg/0.jpeg')
# print(img.shape) # Print image shape
# cv2.imshow("original", img)
# cropped_image = img[98:575,1491:2123]
# cv2.imshow("cropped", cropped_image)
# cv2.imwrite("Cropped Image.jpg", cropped_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# result = subprocess.getoutput(
    # f'--skip-text {file} / {name} {file} / {name}')
    # ocrmypdf.ocr(file + '/' + name, file + '/' + name)

    # if not re.search("PriorOcrFoundError: page already has text!", result):
    #     repaired.append(name)
    # else:
    #     corrupted.append(name)
    # return

# abc = sys.argv[1]
# if os.path.exists(abc):
#     print ('file exist')

# ocrmypdf.ocr('/home/caypro/Documents/ibgcPdfs/IBGC_PDF/IBGC_PDF/IBGC_1192966.pdf','/home/caypro/Documents/ibgcPdfs/IBGC_PDF/IBGC_PDF/IBGC_1192966.pdf')
#subprocess.run(["qpdf", "--replace-input", "/home/caypro/Documents/ibgcPdfs/IBGC_PDF/IBGC_PDF/IBGC_4814325.pdf"])
# def fetch(file):
#     for root, dirs, files in os.walk(file):
#         for name in files:
#             if name.endswith('.pdf'):
#                 subprocess.call(['qpdf','--replace-input',file +'/'+ name])
#                 with open(file+'/'+name, 'rb') as f:
#                     reader  = PyPDF2.PdfFileReader(f)


# ocrmypdf.ocr('/home/caypro/Documents/ibgcPdfs/IBGC_PDF/IBGC_PDF/IBGC_1192966.pdf','/home/caypro/Documents/ibgcPdfs/IBGC_PDF/IBGC_PDF/IBGC_3318460.pdf')
#subprocess.run(["qpdf", "--replace-inpu0t", "/home/caypro/Documents/ibgcPdfs/IBGC_PDF/IBGC_PDF/IBGC_4814325.pdf"])
# print(fetch('/home/caypro/Documents/ibgcPdfs/IBGC_PDF/IBGC_PDF'))
# print(corrupted)
# print(non_corrupted)


# with open (file + '/' + name,'rb')as f:
    #     reader = PyPDF2.PdfFileReader(f)
    #     count = reader.numPages
    #     for i in range(count):
    #         page = reader.getPage(i)
    #         output = page.extractText()

# myPath = os.path.dirname(os.path.realpath(__file__))
# print(myPath)
# with Pdf.open('/home/caypro/Documents/ibgcPdfs/IBGC_PDF/IBGC_PDF/IBGC_4829513.pdf') as pdf:
#      pdf.save(f'{myPath}/output.pdf')

# FileObj = open(f'{myPath}/output.pdf', 'rb')
# # with open(f'{myPath}/output.pdf', 'rb') as f:
# reader = PyPDF2.PdfFileReader(pdfFileObj)
# pageObj = reader.getPage(1)
# # information = reader.getDocumentInfo()
# print(pageObj.extractText())# pdf

# # pdfFileObj.close()

# # from io import StringIO
# # from pdfminer.high_level import extract_text
# # output_string = ""
# # with open('/home/caypro/Documents/ibgcPdfs/IBGC_PDF/IBGC_PDF/IBGC_5913111.pdf', 'r') as fin:
# #     output_string = extract_text(fin)
# # print(output_string)

# def convert_to_jpeg (file):
#     for root,dirs,files in os.walk(file):
#         for name in files:
#             if file.endswith('.pdf'):
#                 pages = convert_from_path(file)
#                 for page in range(len(pages)):
#                     pages[page].save(f'/home/caypro/Documents/ibgc/IBGC_PDF/IBGC_PDF/jpeg/{page}.jpeg')


# pages = convert_from_path(file +'/'+ name, 500)
#                 for page in pages:
#                     # page.save(file +'/'+ name+'.jpeg')
#                     page.save(f"{file}/{name
#                     }.jpeg")
