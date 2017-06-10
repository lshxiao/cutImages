# 1、新建目录，并在目录下创建setup.py文件
```python
# 参考URL： http://liluo.org/blog/2012/08/how-to-create-python-egg/

# 然后创建功能模块，本项目是cutImages包
```


# 2、打包并上传
```python
# 打包
python setup.py sdist bdist_wheel bdist_egg
# sdist: 生成类似 *.tar.gz，支持 pip
# bdist_egg:  生成类似 *.egg，支持 easy_install

# 注册
twine register dist/cutImages-0.1.tar.gz
# 如果没有账号，请自己到https://pypi.python.org/pypi注册， 如果没安装twine，可直接 pip install twine 进行安装

# 上传
twine upload dist/cutImages-0.1.tar.gz
```

# 3、可以通过 pip install cutImages 安装
```python
# 安装
pip install cutImages

# 引用
from cutImages import cut_images


```
