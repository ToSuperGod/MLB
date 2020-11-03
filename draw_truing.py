import cv2
import numpy as np
'''
完结
目标实现
1.人像精修

已实现：
RGB和HSI相互转化
自主调节色调、亮度、饱和度、对比度
生成锐化、浮雕图像
'''


def hue(img_hsi):
    """
    改变色调
    :param img_hsi:
    :return:
    """
    num = 100  # 可调节数值
    # img_hsi[:, :, 0] = img_hsi[:, :, 0] + num
    w = img_hsi.shape[0]
    h = img_hsi.shape[1]
    for i in range(w):
        for j in range(h):
            img_hsi[i, j, 0] = img_hsi[i, j, 0] + num if (img_hsi[i, j, 0] + num >= 255) and (img_hsi[i, j, 0] + num <= 0) else img_hsi[i, j, 0]
    return img_hsi


def emboss(img):
    """
    浮雕效果
    :param img:
    :return:
    """
    kernel = np.array((
        [-2, -1, 0],
        [-1, 1, 1],
        [0, 1, 2],
    ), dtype="float32")
    image = cv2.filter2D(img, -1, kernel)
    res = np.hstack((img, image))
    return res


def sharpen(img):
    """
    自定义内核对图像进行卷积，完成锐化
    :param img:
    :return: res
    """
    kernel = np.array((
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0],
    ), dtype="float32")
    image = cv2.filter2D(img, -1, kernel)
    res = np.hstack((img, image))
    return res


def to_hsi(path):  # 函数转换RGB->HSI
    image = cv2.imread(path)
    img_hsi = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    return img_hsi


def to_rgb(img_hsi):  # 函数转换HSI->RGB
    img_rgb = cv2.cvtColor(img_hsi, cv2.COLOR_HSV2BGR)
    return img_rgb


def saturation(img_hsi):  # 饱和度
    num = 200  # 5~ 100
    img_hsi[:, :, 1] = num / 100.0 * img_hsi[:, :, 1]
    return img_hsi


def img_bright(img_hsi):  # 调节亮度(找黑天拍的图片)
    # print(type(img_hsi))
    num = 150  # 0~200
    img_hsi[:, :, 2] = num / 100.0 * img_hsi[:, :, 2]
    return img_hsi


def img_beta_alpha(img):
    """
    亮度对比度一起调节
    :param img:
    :return: res
    """
    alpha = 1.9  # 对比度 0~2
    beta = 30  # 亮度 0~100
    res = np.uint8(np.clip((alpha * img + beta), 0, 255))
    return res


def main():
    path = "D:/study/TP/2.jpg"
    img = cv2.imread(path)
    # img = emboss(img)  # 浮雕效果
    # img = sharpen(img)  # 锐化操作
    # img = img_beta_alpha(img)  # 亮度和对比度一起调节
    img_hsi = to_hsi(path)
    img_hsi = hue(img_hsi)  # 色调调节
    # img_hsi = img_bright(img_hsi)  # 亮度
    # img_hsi = saturation(img_hsi)  # 饱和度
    img_rgb = to_rgb(img_hsi)
    # cv2.imshow("photo", img)
    cv2.imshow("RGB", img_rgb)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
