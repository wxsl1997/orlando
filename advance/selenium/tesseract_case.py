import pytesseract
from PIL import Image

if __name__ == '__main__':
    im = Image.open('图片-英文.png')
    text = pytesseract.image_to_string(im, lang='eng')
    print(text)
    # 3n3D

    im = Image.open('图片-中文.png')
    text = pytesseract.image_to_string(im, lang='chi_sim')
    print(text)
    # 模 块 安 装
