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

####  下载或克隆本项目至本地目录

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

## 2.1 项目1：获取淘宝首页商品分类

#### 1. 修改pipelines.py

(打开对应的注释关闭同级其他注释即可)

```python
...
class TaobaospiderPipeline(object):
    def __init__(self):
        self.file = codecs.open('class.json', 'wb', encoding='utf-8')
...
```

#### 2. 运行

在`.setting`同级目录下运行：

`scrapy crawl taobao`

(说明：运行的是`taobao.py`文件)

#### 3. 检查结果

生成`class.json`文件，内容如下：

```json
{"class2": ["羽绒服女", "毛呢外套女", "毛衣女", "针织衫女", "棉服女", "连衣裙",  "风衣女装", "裤子女装", "卫衣女装", "T恤女装", "衬衫女装", "半身裙", "西装女", "打底衫女", "夹克女", "皮衣女", "妈妈装","婚纱礼服"], "class1": "女装"}
{"class2": ["外套男装", "夹克男装", "衬衫男装", "T恤男装", "棒球服男装", "牛仔外套男装", "卫衣男装", "西装男", "风衣男装", "皮衣男装", "针织衫男装", "呢大衣男装", "休闲裤男装", "牛仔裤男装", "运动裤男装", "九分裤男装", "马甲男装", "羽绒服男装", "棉衣男", "中老年男装"], "class1": "男装"}
{"class2": ["保暖内衣", "丝绒睡衣", "内裤女", "文胸", "内裤男", "长袖睡衣", "珊瑚绒睡衣", "夹棉睡衣", "长筒袜", "棉袜", "情侣睡衣", "秋裤", "保暖背心", "睡袍", "男士睡衣", "塑身衣", "内衣套装", "打底裤", "连体睡衣", "睡裙女冬", "聚拢文胸", "男士袜子", "棉袜女", "卡通睡衣"], "class1": "内衣"}
...
```

## 2.2 项目2：爬取各个分类下的商品

#### 1. 修改pipelines.py

(打开对应的注释关闭同级其他注释即可)

```python
class TaobaospiderPipeline(object):
    def __init__(self):
        #self.file = codecs.open('class.json', 'wb', encoding='utf-8')
        self.file = codecs.open('yourname.json', 'wb', encoding='utf-8')
```

#### 2. 运行

在`.setting`同级目录下运行：

`scrapy crawl taobaodata`

(说明：运行的是`taobaodata.py`文件)

#### 3. 检查结果

在运行界面看到运行信息：

```
...
{'class1': '\xe5\xa5\xb3\xe8\xa3\x85',
 'class2': '\xe6\xaf\x9b\xe8\xa1\xa3\xe5\xa5\xb3',
 'price': u'89.00',
 'sales': 13000.0,
 'store': u'<',
 'title': u'\u534a\u9ad8\u9886\u52a0\u539a\u751c\u7f8e\u6253\u5e95\u5957\u5934\u
97e9\u7248\u5bbd\u677e\u6bdb\u8863'}
...
```
生成`yourname.json`文件，内容如下：

```json
{"title": "秋冬韩版半高领修身显瘦加厚针织衫", "price": "49.00", "sales": 5557.0, "class2": "毛衣女", "store": "<", "class1": "女装"}
{"title": "秋冬宽松半高领套头学生韩版加厚毛衣", "price": "88.00", "sales": 8771.0, "class2": "毛衣女", "store": "", "class1": "女装"}
...
```

####  其他说明

本项目的保存结果已经全部保存至result文件夹下

---
