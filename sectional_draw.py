import os
import paddlehub as hub

'''
完结
目标实现
1.人像抠图
2.更换底色合成新图片

已实现
1.人像抠图并保存到根目录
'''


def main():  # 单张抠图，创建新的文件夹，图片自动保存到humanseg_output文件
    path = 'D:/study/TP/6.jpg'
    humanseg = hub.Module(name='deeplabv3p_xception65_humanseg')
    imgs = [path]
    results = humanseg.segmentation(data={'image': imgs})


if __name__ == '__main__':
    main()

# humanseg = hub.Module(name='deeplabv3p_xception65_humanseg')
# # 图片文件的目录
# path = 'D:/study/head/'
# # 获取目录下的文件
# files = os.listdir(path)
# # 用来装图片的
# imgs = []
# # 拼接图片路径
# for i in files:
#    imgs.append(path + i)
# #抠图
# results = humanseg.segmentation(data={'image': imgs})

