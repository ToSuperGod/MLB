from PIL import Image, ImageDraw, ImageFont
import cv2
'''
完结

实现：
2.添加中文汉字，可选字体、大小、起始位置、颜色
'''


def add_chinese(path, text, understand):
    image = Image.open(path)
    font = ImageFont.truetype('./font/simhei.ttf', 48)  # 定义字体
    draw = ImageDraw.Draw(image)
    position = (30, 30)  # 位置坐标
    color = (0, 0, 255)
    draw.text(position, text, fill=color, font=font)
    image.save('./images/' + str(understand) + '.jpg')
    img_res = cv2.imread('./images/' + str(understand) + '.jpg')
    return img_res


