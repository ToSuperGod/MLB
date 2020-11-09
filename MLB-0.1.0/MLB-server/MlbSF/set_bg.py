import cv2
import math
import numpy as np
from PIL import Image
import paddlehub as hub
'''
已实现：
更换背景
图像翻转
证件照
'''


def set_background(path, path_t):  # 更换背景图片
    print(path_t)
    img_bg = Image.open(path_t)
    image = Image.open(path)
    w = image.width
    h = image.height
    img_bg = img_bg.resize((w, h))  # 宽高一致
    r, g, b, a = image.split()
    img_bg = img_bg.copy()
    img_bg.paste(image, (0, 0), mask=a)
    res = np.array(img_bg.convert('RGB'))[:, :, ::-1]
    return res


def set_back_color(path, flag):
    img = Image.open(path)
    w = img.width
    h = img.height
    r, g, b, a = img.split()
    if flag:
        color_ = (0, 0, 255)  # 更换背景颜色
    else:
        color_ = (255, 0, 0)  # 更换背景颜色
    img_back = Image.new('RGB', (w, h), color_)
    img_back.paste(img, (0, 0), mask=a)
    # img_back = img_back.resize((256, 256))
    img_res = np.array(img_back.convert('RGB'))[:, :, ::-1]
    return img_res


def img_transfer(path_t):
    img = cv2.imread(path_t)
    image3 = img[:, ::-1, :]
    cv2.imshow("res", image3)
    cv2.waitKey(0)


def get_people(path):
    humanseg = hub.Module(name='deeplabv3p_xception65_humanseg')
    imgs = [path]
    results = humanseg.segmentation(data={'image': imgs})
    return True

