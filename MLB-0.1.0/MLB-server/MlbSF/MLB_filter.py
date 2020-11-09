import cv2
import numpy as np
import math
'''
完结
实现:多种滤镜
'''


def all_filter(img, b, g, r):  # 夕阳滤镜
    w = img.shape[0]
    h = img.shape[1]
    # 改变这三个值改变色调
    for i in range(w):
        for j in range(h):
            img[i, j, 0] = int(img[i, j, 0] * b) if int(img[i, j, 0] * b) <= 255 else 255
            img[i, j, 1] = int(img[i, j, 1] * g) if int(img[i, j, 1] * g) <= 255 else 255
            img[i, j, 2] = int(img[i, j, 2] * r) if int(img[i, j, 2] * r) <= 255 else 255
    return img


def old_pic(image):
    """
    复古风格
    :param image:
    :return:
    """
    rows, cols, channals = image.shape
    for r in range(rows):
        for c in range(cols):
            B = image.item(r, c, 0)
            G = image.item(r, c, 1)
            R = image.item(r, c, 2)
            image[r, c, 0] = np.uint8(min(max(0.272 * R + 0.534 * G + 0.131 * B, 0), 255))
            image[r, c, 1] = np.uint8(min(max(0.349 * R + 0.686 * G + 0.168 * B, 0), 255))
            image[r, c, 2] = np.uint8(min(max(0.393 * R + 0.769 * G + 0.189 * B, 0), 255))
    return image


def pencil(image):  # 铅笔画, 黑白, 彩铅
    dst_gray, dst_color = cv2.pencilSketch(image, sigma_s=50, sigma_r=0.15, shade_factor=0.04)
    return dst_gray, dst_color


def cartoon(image):  # 卡通画
    dst_comic = cv2.stylization(image, sigma_s=60, sigma_r=0.07)
    return dst_comic


def filter_convex(src_img):  # 凸透镜,中心点选择原始图片中点
    """
    实现凸透镜效果
    :param src_img:
    :return:
    """
    row = src_img.shape[0]
    col = src_img.shape[1]
    channel = src_img.shape[2]
    new_img = np.zeros([row, col, channel], dtype=np.uint8)
    center_x = row/2
    center_y = col/2
    # radius=math.sqrt(center_x*center_x+center_y*center_y)/2
    radius = min(center_x, center_y)
    for i in range(row):
        for j in range(col):
            distance = ((i-center_x)*(i-center_x)+(j-center_y)*(j-center_y))
            new_dist = math.sqrt(distance)
            new_img[i, j, :] = src_img[i, j, :]
            if distance <= radius**2:
                new_i = np.int(np.floor(new_dist*(i-center_x)/radius+center_x))
                new_j = np.int(np.floor(new_dist*(j-center_y)/radius+center_y))
                new_img[i, j, :] = src_img[new_i, new_j, :]
    return new_img


def dodge(image, mask):  # 亮化操作
    return cv2.divide(image, 255 - mask, scale=256)


def burn(image, mask):  # 暗化操作
    return 255 - cv2.divide(255 - image, 255 - mask, scale=256)


def around(image):  # 素描效果
    """
    实现素描效果
    :param path:
    :return:
    """
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 将图片转换到灰度空间
    img_gray_inv = 255 - img_gray  # 灰度反色操作
    img_blur = cv2.blur(img_gray_inv, (10, 10))  # 图像平滑
    img_res = dodge(img_gray, img_blur)
    return img_res
