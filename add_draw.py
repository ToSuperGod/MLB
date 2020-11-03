import cv2
import numpy as np
from PIL import Image

'''
完结

目标实现：
1、图片指定位置添加贴纸
2、虚拟背景

已实现：
1.真爱我她，与恋人图片重影，程度可调  add_love（函数可以换，用PIL的）
2.在指定区域用指定图片覆盖  add_picture(有多种方法)
'''

'''
注意：
1.cv2.add() 要求图片大小相同
2.cv2.addWeighted(img, 0.7, img_vir, 0.3, 0)  带权重叠加
3.img.paste()  图片覆盖
4.Image.blend(image1,image2, alpha)  alpha为透明度，此函数为合成一张新的图片
5.Image.composite()  插值出一张新的图片
6.img_blur[0:, 0:] = img_vir  也是指定区域覆盖方法
'''


def add_picture(path, path_t):
    img = Image.open(path)
    mark = Image.open(path_t)  # 覆盖图
    mark = mark.crop((50, 50, 100, 100))  # 裁剪覆盖图
    img.paste(mark, (100, 100, 150, 150))  # 覆盖区域大小要和mark大小一致
    img.show()


def virtual_background(path, path_t):  # 抠图和原图数组一样
    img = cv2.imread(path, 1)
    img_vir = cv2.imread(path_t, 1)
    img_blur = cv2.GaussianBlur(img, (101, 101), 0)  # 高斯模糊
    # res = cv2.(img_blur, img_vir)
    img_blur[0:, 0:] = img_vir
    cv2.namedWindow("photo", cv2.WINDOW_NORMAL)
    cv2.imshow("photo", img_blur)
    cv2.waitKey(0)


def add_logo(path, path_t):
    img = Image.open(path)
    mark = Image.open(path_t)


def add_love(path, path_t):
    img = cv2.imread(path)
    img_vir = cv2.imread(path_t)
    w = img.shape
    img_vir = cv2.resize(img_vir, (w[1], w[0]))
    res = cv2.addWeighted(img, 0.7, img_vir, 0.3, 0)  # 调节重影程度
    cv2.namedWindow("photo", cv2.WINDOW_NORMAL)
    cv2.imshow("photo", res)
    cv2.waitKey(0)


def main():
    path = "D:/study/TP/2.jpg"
    path_t = "./humanseg_output/2.png"  # 叠加照片
    # path_t = "D:/study/TP/2.jpg"
    # add_picture(path, path_t)  # 裁剪指定区域相加
    virtual_background(path, path_t)
    # add_logo(path, path_t)  #
    # add_love(path, path_t)  # 真爱我她，自己与恋人图片重影


if __name__ == '__main__':
    main()

