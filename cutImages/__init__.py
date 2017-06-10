# coding=utf-8
import os
from PIL import Image

__author__ = 'lshxiao'

'''
old_path: 原图片目录
new_path: 剪切之后的图片目录, 如果不存在, 会自动创建。 另外会保存一个不剪切的图片目录, 详见代码
width: 剪切之后的图片宽度
height: 剪切之后的图片高度
quality: 图片保存的质量, 1~100之间的数字, 数字越小质量越差
'''
def cut_images(old_path, new_path, width, height, quality):
    f_list = os.listdir(old_path)
    if not os.path.exists(new_path):
        os.makedirs(new_path, 0755)
    for i, f in enumerate(f_list):
        end_type = os.path.splitext(f)[1].lower()
        if os.path.isdir(old_path + '/' + f):
            pass
        elif end_type in ['.jpg', '.jpeg', '.png', '.gif']:
            print i + 1
            try:
                make_thumbnail(old_path, new_path, f, width, height, quality)
            except Exception, e:
                print Exception, e
                # 如果图片很多, 一次执行不完, 最好是分批剪切, 也可以把已经压缩过的图片给删除
                # os.remove(old_path+'/'+f)


def make_thumbnail(old_path, new_path, f, w, h, quality):
    path = old_path + '/' + f
    # convert('RGB')这个必须加上, 否则可能会报错: cannot write mode P as JPEG
    icon = Image.open(path).convert('RGB')
    width, height = icon.size
    print width, height
    # 只切高度大于宽度的图片, 宽度大于高度的图片复制到另一个目录
    if width < height:
        icon = icon.resize((500, int(500 * height / width)), Image.ANTIALIAS)
    else:
        icon = icon.resize((int(500 * width / height), 500), Image.ANTIALIAS)
    icon = icon.crop((0, 0, int(w), int(h)))
    print new_path + '/' + f
    icon.save(new_path + '/' + f, 'jpeg', quality=quality)


# demo 示例
# cut_images('/Users/lshxiao/Desktop/old_images', '/Users/lshxiao/Desktop/new_img', 500, 500, 50)
