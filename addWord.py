# 添加文字
import cv2
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
'''
完结

实现：
1.添加英文文字，可以选择文字颜色、起始位置、字体大小、文字粗细、字体
2.添加中文汉字，可选字体、大小、起始位置、颜色
'''


def add_english(path):
    image = cv2.imread(path)
    text = "Hello Miss.Min"  # 设置添加的文字
    position = (10, 100)  # 设置文字的起始位置
    font_size = 3  # 设置字体大小
    font_color = (0, 0, 255)  # 文字颜色

    font = cv2.FONT_HERSHEY_SIMPLEX  # 默认字体  圆润
    font1 = cv2.FONT_HERSHEY_COMPLEX  # 字体不同  电脑体
    font2 = cv2.FONT_HERSHEY_COMPLEX_SMALL  # 小版电脑体
    font3 = cv2.FONT_HERSHEY_DUPLEX  # 圆润
    font4 = cv2.FONT_HERSHEY_PLAIN  # 小圆润
    font5 = cv2.FONT_HERSHEY_SCRIPT_COMPLEX  # 硬连笔
    font6 = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX  # 软连笔
    font7 = cv2.FONT_HERSHEY_TRIPLEX  # 正版

    thickness = 2  # 字体粗细,只直径大小
    cv2.putText(image, text, position, font5, font_size, font_color, thickness, cv2.LINE_AA)
    # cv2.namedWindow("photo", cv2.WINDOW_NORMAL)
    cv2.imshow("photo", image)
    cv2.waitKey(0)


def add_chinese(path):
    image = Image.open(path)
    font = ImageFont.truetype('./font/simhei.ttf', 48)  # 定义字体
    draw = ImageDraw.Draw(image)
    position = (100, 100)  # 位置坐标
    text = '你好，闵小姐sdfasdfasfasdf'
    color = (0, 0, 255)
    draw.text(position, text, fill=color, font=font)
    # plt.imshow(image)
    Image._show(image)


def main():
    path = 'D:/study/TP/1.jpg'
    # add_english(path)
    add_chinese(path)


if __name__ == '__main__':
    main()
