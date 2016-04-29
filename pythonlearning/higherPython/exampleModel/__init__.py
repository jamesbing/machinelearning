#!/usr/bin/env python
# coding=utf-8

'写在一个模块的这个位置的注释表示该模块的文档注释，任何代码块的第一个字符串都会被当做是一个模块的文档注释。所以这儿应该写：example model,这里是一个标准的文件模板'

__author__='James Leng' #这个位置用于标识作者，开源软件中，此处相当于是我自己的签名

import sys

def test():
    args = sys.argv
    if(len(args) == 1):
        print 'Hello world'
    elif(len(args) == 2):
        print 'Hello, %s!' % args[1]
    else:
        print 'Too many arguments!'

if __name__ == '++main++':
    test()

