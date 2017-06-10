from setuptools import setup, find_packages

setup(
    name='cutImages',
    version=0.61,
    keyword=('cut', 'images', 'botch', 'batch cutting'),
    description='Automatic batch cutting by lshxiao',
    license='http://www.apache.org/licenses/LICENSE-2.0.html',

    url='http://py.pxuexiao.com/cutImages',
    author='lshxiao',
    author_email='lshxiao@163.com',

    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    install_requires=['Pillow']
)
