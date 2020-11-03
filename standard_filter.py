import cv2
import numpy as np
import math
'''
完结
目标实现
有滤镜基色卡，转换公式
b, g, r = src_img[i][j]
x = int(g / 4 + int(b / 32) * 64)
y = int(r / 4 + int(b % 32) * 64)

已实现：
凸透镜
凹透镜为C++实现不知道可否连接
'''


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
    cv2.imshow("new", new_img)
    cv2.waitKey()
    # return new_img


def azimuthAngle(x1, y1, x2, y2):
    """
    忘记什么函数
    :param x1:
    :param y1:
    :param x2:
    :param y2:
    :return:
    """
    angle = 0.0
    dx = x2 - x1
    dy = y2 - y1
    if x2 == x1:
        angle = math.pi / 2.0
        if y2 == y1:
            angle = 0.0
        elif y2 < y1:
            angle = 3.0 * math.pi / 2.0
    elif x2 > x1 and y2 > y1:
        angle = math.atan(dx / dy)
    elif x2 > x1 and y2 < y1:
        angle = math.pi / 2 + math.atan(-dy / dx)
    elif x2 < x1 and y2 < y1:
        angle = math.pi + math.atan(dx / dy)
    elif x2 < x1 and y2 > y1:
        angle = 3.0 * math.pi / 2.0 + math.atan(dy / -dx)
    return angle * 180 / math.pi


def filter_concave(img):
    row = img.shape[0]
    col = img.shape[1]
    channel = img.shape[2]
    new_img = np.zeros([row, col, channel], dtype=np.uint8)
    center_x = row // 2
    center_y = col // 2
    for i in range(row):
        for j in range(col):
            theta = azimuthAngle(center_x, center_y, i, j)
            x = [i-center_x, j-center_y]
            R = np.linalg.norm(x=x) * 8  # 范数
            new_x = center_x + int(R*math.cos(theta))
            new_y = center_y + int(R*math.sin(theta))
            if new_x < 0: new_x = 0
            elif new_x >= col: new_x = col - 1
            if new_y < 0: new_y = 0
            elif new_y >= row: new_y = row - 1
            # 差一点东西不会了


def main():
    path = 'D:/study/TP/1.jpg'
    src_img = cv2.imread(path)
    filter_convex(src_img)  # 凸透镜
    # filter_concave(src_img)  # 凹透镜


if __name__ == '__main__':
    main()
