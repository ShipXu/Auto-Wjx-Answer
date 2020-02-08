# Auto-Wjx-Answer
项目的主要目的就是自动完成问卷星调查报告

# Readme
目前完成的是基础版本，主要先解决了作者自己填写报告的问题，即与疫情相关问题为否的情况。填写内容，包括问卷中的[1,2,3,4,5,15,17,19,21,22,23,28]。其中，[5,15,17,19,21,22,23,28]答案均为否。

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

## 内容列表
- [用于吐槽的前言](#吐槽)
- [主要技术背景](#主要技术背景)
- [详细实现](#详细实现)
- [运行环境准备](#运行环境准备)
- [运行方法](#运行方法)

## 用于吐槽的前言
项目的主要目的就是hack自动问卷星调查报告这个任务。最近两次被老板叫起床填报告，真的是被吓怕了orz。作为一只懒惰的程序员，我真的是不想填表啊。出于这样的懒惰，虽然今年做了很久的调参boy，但想想自己以前居然也做过网站。为啥不试试用计算机网络的知识自动提交这个报告呢(装X想法涌入大脑)。后来发现根本不用计算机网络的东西，用python工具+前端思想就可以解决这个问题。(python大法好)

但是过程中还是碰到一些有趣的设计和实现上的问题，所以记录一下，也算是蛮有趣的一起hack经历。如果对实现部分没兴趣，可以直接跳到准备部分+运行部分


## 主要技术背景
- 前端知识: 少量前端的知识，主要需要回顾一下html里面的一些控件，同时对html文件的基本结构有个基本的把握就可以;
- [Xpath](https://zh.wikipedia.org/wiki/XPath):用于定位网页中的控件;
- Selenium: Selenium是一个用于测试网页程序的程序，它的另外一个作用是做为爬虫时的工具，用于在代码中与网页进行交互;[Selenium-python的官方文档](https://selenium-python-zh.readthedocs.io/en/latest/index.html);


## 详细实现
[待续]


## 运行环境准备
准备部分主要是将脚本中自己的信息给修改掉，并且需要下载浏览器的驱动并填写驱动所在的路径至脚本中。

- 首先，chrome用户需下载驱动至脚本同一目录下，其中驱动版本需要和chrome版本对齐。
[Chrome驱动下载地址](https://sites.google.com/a/chromium.org/chromedriver/downloads)
(使用git下载的用户，文件夹中有包含相关驱动)
- 安装selenium模块: pip install selenium
- 然后，根据个人信息修改answer-sheet.txt的内容。

![image](https://github.com/ShipXu/Auto-Wjx-Answer/blob/master/images/person%20info.JPG)



## 运行方法
在控制台运行Auto_WJX_Answer.py，具体命令格式如下，运行时需指定：
```
usage: Auto_WJX_Answer.py [-h] [-d DRIVER] url

positional arguments:
  url                   the questionary website

optional arguments:
  -h, --help            show this help message and exit
  -d DRIVER, --driver-path DRIVER
                        the driver path
```
