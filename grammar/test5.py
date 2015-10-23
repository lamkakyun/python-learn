#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"测试 process 2"
__author__ = 'AWT'

import os
import multiprocessing

def info(title):
    print(title)
    print('module name: ', __name__)
    if hasattr(os, 'getppid'):
        print('parent process: ', os.getppid()) # 父程式是shell（zsh）
    print('process id: ', os.getpid())

def hello(name):
    info('function hello')
    print('hello', name)

if __name__ == '__main__':
    info('main line')
    p = multiprocessing.Process(target=hello, args=('',))
    p.start()
    p.join()