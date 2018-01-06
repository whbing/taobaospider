# 1. 运行环境
1. python 2.7 
2. Scrapy 1.4.0

## 1.2 环境搭建过程

#### 1. 确保已有python环境。

```python

$python
Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:24:40) [MSC v.1500 64 bit (AMD64)] on win32
>>>

```

#### 2. 安装pip

或其他包管理工具也可以

windows:点击https://pypi.python.org/pypi/pip 下载pip-x.y.z.tar.gz (md5, pgp)

解压后进入文件夹执行：`python setup.py install`

或者直接下载exe文件进行安装，下载地址为：http://www.lfd.uci.edu/~gohlke/pythonlibs/#pip

#### 3.安装lxml

lxml是一种使用 Python 编写的库，可以迅速、灵活地处理 XML。选择对应的Python版本安装。

安装命令：`pip install lxml`

验证是否安装成功：`>>>import lxml`

#### 4.安装zope.interface，安装命令：
`pip install zope.interface`
 
#### 5.安装Twisted

Twisted是用Python实现的基于事件驱动的网络引擎框架，安装命令： 

`pip install twisted` 

#### 6.安装pyOpenSSL

pyOpenSSL是Python的OpenSSL接口，安装命令：

`pip install pyopenssl`

#### 7.安装win32py （windows需要）

提供win32api，点击 http://sourceforge.net/projects/pywin32/files/pywin32/ 下载

#### 8.安装Scrapy

`pip install scrapy`

并将scrapy加入环境变量

#### 9.测试是否scrapy可用:

`scrapy bench`

安装完成

---

# 2. 本项目的运行

#### 2.1 下载或克隆本项目至本地目录

目录结构(主要)：

```
taobaospider(or your folder)
	|
	|-scrapy.cfg
	|-.settings
	|-result
	|-taobaospider
		   |
		   |-__init__.py
		   |-items.py
		   |-middlewares.py
		   |-pipelines.py
		   |-settings.py
		   |-spiders
		       |
		       |-__init__.py
		       |-taobao.py
		       |-taobaodata.py
		       

```