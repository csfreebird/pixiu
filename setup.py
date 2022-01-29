# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @author :deanFB
# blog: blog.csdn.net/csfreebird

import setuptools

setuptools.setup(
    # 指定项目名称，我们在后期打包时，这就是打包的包名称，当然打包时的名称可能还会包含下面的版本号哟~
    name='pixiu',
    # 指定版本号
    version='0.1.0',
    # 这是对当前项目的一个描述
    description='一个关于A股下载和计算的python工具包',
    # 作者是谁，指的是此项目开发的人，这里就写你自己的名字即可
    author='deanFB',
    # 作者的邮箱
    author_email='dean-chen@qq.com',
    # 写上项目的地址，比如你开源的地址开源写博客地址，也开源写GitHub地址，自定义的官网地址等等。
    url='https://github.com/csfreebird/pixiu',
    # 指定包名，即你需要打包的包名称，要实际在你本地存在哟，它会将指定包名下的所有"*.py"文件进行打包哟，但不会递归去拷贝所有的子包内容。
    packages=setuptools.find_packages()
)
