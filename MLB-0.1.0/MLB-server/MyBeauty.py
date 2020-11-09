from flask import Flask, request
import base64
import cv2
import numpy as np
import re
from MlbSF import MLB_filter,whileFace,draw_truing,add_word,thin_face,set_bg
import time
import shutil
import os
app = Flask(__name__)
understand = 0  # 处理标准
num_extent = 0  # 处理强度
path_s = ''  # 背景图片路径
add_text = ''  # 添加文字文本
save_img = []  # 保存处理后的图片
original_img = []  # 保存原始图片


def transfer():
    while understand:
        img = original_img[0]
        if understand == 1:  # 一键美白
            img_while = whileFace.buffing(img)
            save_img.append(img_while)
            print("美颜处理")
            break
        elif understand == 2:  # 复古风格
            img_old = MLB_filter.old_pic(img)
            save_img.append(img_old)
            print("复古风格处理")
            break
        elif understand == 3:
            img_cartoon = MLB_filter.cartoon(img)
            save_img.append(img_cartoon)
            print("卡通画处理")
            break
        elif understand == 4:
            img_pencil_gary, img_pencil_color = MLB_filter.pencil(img)
            save_img.append(img_pencil_gary)
            print("铅笔画处理")
            break
        elif understand == 5:
            img_pole = MLB_filter.all_filter(img, 1, 0.8, 0.8)
            save_img.append(img_pole)
            print("北极寒处理")
            break
        elif understand == 6:
            img_green = MLB_filter.all_filter(img, 0.9, 1, 0.9)
            save_img.append(img_green)
            print("艾草绿处理")
            break
        elif understand == 7:
            img_convex = MLB_filter.filter_convex(img)
            save_img.append(img_convex)
            print("放大镜处理")
            break
        elif understand == 8:
            img_around = MLB_filter.around(img)
            save_img.append(img_around)
            print("素描处理")
            break
        elif understand == 9:
            img_hue = MLB_filter.all_filter(img, 0.8, 0.8, 1)
            save_img.append(img_hue)
            print("樱花滤镜处理")
            break
        elif understand == 10:
            img_sharpen = draw_truing.sharpen(img)
            save_img.append(img_sharpen)
            print("锐化处理")
            break
        elif understand == 11:
            img_emboss = draw_truing.emboss(img)
            save_img.append(img_emboss)
            print("浮雕处理")
            break
        elif understand == 12:
            shutil.rmtree('./images')
            os.mkdir('./images')
            cv2.imwrite('./images/' + str(understand) + '.jpg', img)
            path = './images/' + str(understand) + '.jpg'
            img_hue = draw_truing.true_all_hue(path, num_extent)
            save_img.append(img_hue)
            print("色调调节")
            break
        elif understand == 13:
            shutil.rmtree('./images')
            os.mkdir('./images')
            cv2.imwrite('./images/' + str(understand) + '.jpg', img)
            path = './images/' + str(understand) + '.jpg'
            img_bright = draw_truing.true_all_bright(path, num_extent)
            save_img.append(img_bright)
            print("亮度调节")
            break
        elif understand == 14:
            shutil.rmtree('./images')
            os.mkdir('./images')
            cv2.imwrite('./images/' + str(understand) + '.jpg', img)
            path = './images/' + str(understand) + '.jpg'
            img_saturation = draw_truing.true_all_saturation(path, num_extent)
            save_img.append(img_saturation)
            print("饱和度调节")
            break
        elif understand == 15:
            shutil.rmtree('./images')
            os.mkdir('./images')
            cv2.imwrite('./images/' + str(understand) + '.jpg', img)
            path = './images/' + str(understand) + '.jpg'
            img_word = add_word.add_chinese(path, add_text, understand)
            print("img_word", img_word)
            save_img.append(img_word)
            print("添加文字")
            break
        elif understand == 16:
            img_thin = thin_face.face_thin_auto(img, num=90)  # 取值 10~250
            save_img.append(img_thin)
            print("瘦脸处理")
            break
        elif understand == 17:
            shutil.rmtree('./images')
            shutil.rmtree('./humanseg_output')  # 清空图像输出文件夹
            os.mkdir('./images')
            cv2.imwrite('./images/' + str(understand) + '.jpg', img)
            path = './images/' + str(understand) + '.jpg'
            if set_bg.get_people(path):
                path_t = './humanseg_output' + str(understand) + '.png'
                img_bluer = set_bg.set_back_color(path_t, 1)
                save_img.append(img_bluer)
                print("蓝底证件照处理")
            else:
                print("蓝底处理失败")
            break
        elif understand == 18:
            shutil.rmtree('./images')
            shutil.rmtree('./humanseg_output')  # 清空图像输出文件夹
            os.mkdir('./images')
            cv2.imwrite('./images/' + str(understand) + '.jpg', img)
            path = './images/' + str(understand) + '.jpg'
            if set_bg.get_people(path):
                path_t = './humanseg_output/' + str(understand) + '.png'
                img_red = set_bg.set_back_color(path_t, 0)
                save_img.append(img_red)
                print("红底证件照处理")
            else:
                print("红底处理失败")
            break
        elif understand == 19:
            shutil.rmtree('./images')
            shutil.rmtree('./humanseg_output')  # 清空图像输出文件夹
            os.mkdir('./images')
            cv2.imwrite('./images/' + str(understand) + '.jpg', img)
            path = './images/' + str(understand) + '.jpg'
            if set_bg.get_people(path):
                path_t = './humanseg_output/' + str(understand) + '.png'  # 人像路径
                print("地址path_t", path_t)
                global path_s
                print("地址path_s", path_s)
                img_back = set_bg.set_background(path_t, path_s)  # 原图路径  背景图路径
                save_img.append(img_back)
                path_s = ""
                print("更换背景处理")
            else:
                print("更换背景失败")
            break
        elif understand == 20:  # 还未加瘦脸（最好C++实现，先瘦脸再磨皮）
            img_while = whileFace.beauty_face(img)
            save_img.append(img_while)
            print("超级美颜")
            break
        else:
            print("无该信号")
            break


@app.route('/get_word', methods=['POST', 'GET'])
def get_word():
    """
    得到添加的文字，文字颜色，位置信息
    :return:
    """
    my_word = request.form.get('Text')
    global add_text
    add_text = my_word
    print("获得的文字", add_text)
    return "200"


@app.route('/my_signal', methods=['POST', 'GET'])
def my_signal():
    """
    接收前端处理信号
    :return: 200
    """
    deal_signal = request.get_data()
    deal_signal = str(deal_signal, 'utf-8')
    num = int(deal_signal[6:])
    print("处理信号：", num)
    global understand
    understand = num
    transfer()
    return "200"


def deal_base64(img_bytes):
    img_base = str(img_bytes, 'utf-8')
    img_base = re.sub('%2F', '/', img_base)
    img_base = re.sub('%2B', '+', img_base)
    img_base = re.sub('%3D', '=', img_base)
    img_base = bytes(img_base, encoding='utf8')
    # print("我的base64格式", img_base)
    img_padding = 4 - len(img_base) % 4
    # print("img_paddding", img_padding)
    if img_padding:
        img_base += b'=' * img_padding
    # print("base64 % 4 = ", len(img_base) % 4)
    # print("处理后的base64", img_base)
    img_b64decode = base64.b64decode(img_base)
    img_array = np.frombuffer(img_b64decode, np.uint8)  # 转换np序列
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)  # 转换Opencv格式
    return img


@app.route('/my_get', methods=['POST', 'GET'])
def my_get():
    """
    接收前端发来的图片
    :return: 返回200
    """
    original_img.clear()
    img_bytes = request.get_data()
    img_bytes = img_bytes[7:]
    img = deal_base64(img_bytes)
    original_img.append(img)
    print("图片正确！")
    return "200"


@app.route('/other_image', methods=["POST", "GET"])
def other_image():
    img_bytes = request.get_data()
    img_bytes = img_bytes[11:]    img = deal_base64(img_bytes)
    cv2.imwrite('./static/images/back.jpg', img)
    global path_s
    path_s = './static/images/back.jpg'
    return "200"


@app.route('/my_extent', methods=["POST", "GET"])
def my_extent():
    """
    接收处理强度
    :return:
    """
    deal_intensity = request.get_data()
    deal_intensity = str(deal_intensity, 'utf-8')
    deal_intensity = deal_intensity[4:]
    global num_extent
    num_extent = int(deal_intensity)
    print("处理强度：", num_extent)
    return "200"


@app.route('/my_send', methods=["POST", "GET"])
def my_send():
    """
    向前端发送处理好的图片
    :return: base64编码图片
    """
    img_stream = ''
    # print("save_img", save_img)
    while not save_img:
        time.sleep(1)
    while save_img:
        # print("处理后的图片为：", save_img)
        print("正在发送处理后图片")
        img = save_img.pop()
        global understand
        cv2.imwrite('./static/' str(understand) + '.jpg', img)
        path = './static/' + str(understand) + '.jpg'
        with open(path, 'rb') as img_f:
            img_stream = img_f.read()
            img_stream = base64.b64encode(img_stream)
        print("图片已发送至前端")
        return img_stream
    return "200"


if __name__ == '__main__':
    app.run("0.0.0.0")
