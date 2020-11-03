import cv2

'''
目标实现：
1.涂鸦  https://www.jb51.net/article/157297.htm
'''


def draw_line(path):
    img = cv2.imread(path)
    color = (0, 0, 0)
    cv2.line(img, (20, 20), (40, 50), color, 3)
    cv2.imshow("photo", img)
    cv2.waitKey(0)


def main():
    path = 'D:/study/TP/1.jpg'
    draw_line(path)
    pass


if __name__ == '__main__':
    main()
