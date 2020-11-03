import cv2
import numpy as np

'''
完结
实现
1.素描画与OpenCV自带滤镜
素描画可以使用，自带滤镜部分可以使用

有滤镜基色卡，转换公式
b, g, r = src_img[i][j]
x = int(g / 4 + int(b / 32) * 64)
y = int(r / 4 + int(b % 32) * 64)

'''


def dodge(image, mask):  # 亮化操作
    return cv2.divide(image, 255 - mask, scale=256)


def burn(image, mask):  # 暗化操作
    return 255 - cv2.divide(255 - image, 255 - mask, scale=256)


def around(path):  # 素描效果
    """
    实现素描效果
    :param path:
    :return:
    """
    # 读取图片
    img_rgb = cv2.imread(path, 1)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)  # 将图片转换到灰度空间
    img_gray_inv = 255 - img_gray  # 灰度反色操作
    img_blur = cv2.blur(img_gray_inv, (10, 10))  # 图像平滑
    img_res = dodge(img_gray, img_blur)
    cv2.namedWindow("res", cv2.WINDOW_NORMAL)
    cv2.imshow("res", img_res)
    cv2.waitKey(0)


def beauty(path):
    """
    cv中自带滤镜
    :param path:
    :return:
    """
    img_gray = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    cv2.namedWindow("photo", cv2.WINDOW_NORMAL)
    cv2.imshow("photo", img_gray)
    cv2.waitKey(0)
    img_color = cv2.applyColorMap(img_gray, 10)  # 为cv中的伪彩色函数  改变value值,改变风格,取值范围0~11  1 8 10 可尝试使用
    cv2.namedWindow("photo", cv2.WINDOW_NORMAL)
    cv2.imshow("photo", img_color)
    cv2.waitKey(0)


def main():
    path = "D:/study/TP/4.jpg"
    around(path)  # 素描效果
    # beauty(path)  # OpenCV自带滤镜效果，几乎不能使用


if __name__ == '__main__':
    main()
