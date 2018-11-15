# fast_dueros
fast_dueros 是百度dueros语音交互技能快速开发框架。框架主逻辑引用来自 [bot-sdk-python](https://github.com/jokenwang/bot-sdk-python) 项目。

# 功能简介
	1、Dueros智能音箱技能开发
	2、支持技能本地调试
	3、自动打包ZIP函数包
	4、百度CFC函数包一键上传
# 使用说明
## 第一步
	$ git clone https://github.com/imzeali/fast_dueros.git
	$ pip install -r requirements.txt
## 第二步
#### 配置百度云秘钥
	$ vi config.py 
```
# 百度云后台获取
AK = 'xxxxxxxxx'
# 百度云后台获取
SK = 'xxxxxxxxxx'
# CFC 函数名称
FUNCTION_NAME = 'xxxxxxxx'
# 打包忽略文件
IGNORE_FILES = ['.git', '.idea', '.DS_Store', '.DS_Store', '.gitignore', 'baidubce', 'Crypto.zip']
```
## 第三步
#### 编写技能主逻辑
	$ vi index.py

## 第四步
#### 打包并上传技能
	$ python packaging.py
	CFC zip packaging successful.
	CFC zip update successful.
## 其他
[获取百度云秘钥](https://cloud.baidu.com/doc/Reference/GetAKSK.html#.E5.A6.82.E4.BD.95.E8.8E.B7.E5.8F.96AK.20.2F.20SK)

[百度CFC配置教程](https://cloud.baidu.com/doc/CFC/BestPractise.html#.E4.BB.8E.E5.A4.B4.E5.88.9B.E5.BB.BA.E5.87.BD.E6.95.B0)
