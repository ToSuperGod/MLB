import cv2
import numpy as np
'''
完结
实现:
1.铅笔画、彩铅画、卡通画、复古滤镜
2.夕阳滤镜
'''


def hue(img):  # 各种滤镜
    w = img.shape[0]
    h = img.shape[1]
    # 改变这三个值改变色调
    b = 1
    g = 0.8
    r = 0.8
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


def pencil(image):  # 铅笔画
    dst_gray, dst_color = cv2.pencilSketch(image, sigma_s=50, sigma_r=0.15, shade_factor=0.04)
    return dst_gray, dst_color


def cartoon(image):  # 卡通画
    dst_comic = cv2.stylization(image, sigma_s=60, sigma_r=0.07)
    return dst_comic


if __name__ == '__main__':
    path = 'D:/study/TP/1.jpg'
    save_path = 'D:/study/TP/res/1res.jpg'
    img = cv2.imread(path)

    img_filter = hue(img)  # 滤镜 通过该变rgb数值实现
    cv2.namedWindow("res", cv2.WINDOW_NORMAL)
    cv2.imshow("res", img_filter)
    cv2.waitKey(0)

    # img_res = cartoon(img)  # 卡通画
    # cv2.namedWindow("res", cv2.WINDOW_NORMAL)
    # cv2.imshow("res", img_res)
    # cv2.waitKey(0)
    #
    # res_gray, img_color = pencil(img)  # 铅笔画  与  有色铅笔画
    # cv2.namedWindow("res", cv2.WINDOW_NORMAL)
    # cv2.imshow("res", res_gray)
    # cv2.waitKey(0)
    # cv2.namedWindow("res", cv2.WINDOW_NORMAL)
    # cv2.imshow("res", img_color)
    # cv2.waitKey(0)
    #
    # res_old = old_pic(img)  # 复古风格
    # cv2.namedWindow("res", cv2.WINDOW_NORMAL)
    # cv2.imshow("res", res_old)
    # cv2.waitKey(0)
    # cv2.imwrite(save_path, img_color)
