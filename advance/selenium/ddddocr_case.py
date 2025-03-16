import ddddocr

if __name__ == '__main__':
    ocr = ddddocr.DdddOcr()
    with open('图片-英文.png', 'rb') as fp:
        img_bytes = fp.read()
        result = ddddocr.DdddOcr().classification(img_bytes)
        print(result)
        # 3n3d
