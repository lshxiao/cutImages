
# 一、使用方法
```python
# 1、安装
pip install cutImages

# 2、引用
from cutImages import cut_images

# 3、调用
cut_images('/Users/fybao/Desktop/old_images', '/Users/fybao/Desktop/new_img', 500, 500, 50)

# 4、参数说明
old_path: 原图片目录;
new_path: 剪切之后的图片目录, 如果不存在, 会自动创建。 另外会保存一个不剪切的图片目录, 详见代码;
width: 剪切之后的图片宽度;
height: 剪切之后的图片高度;
quality: 图片保存的质量, 1~100之间的数字, 数字越小质量越差;
```

也可以点击介绍文档: http://py.pxuexiao.com/cutImages

> 如果使用过程有问题, 请联系我
> author: lshxiao
> blog: http://web.pxuexiao.com