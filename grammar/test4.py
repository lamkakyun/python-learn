#!/usr/bin/env python
# -*- coding: UTF-8 -*-
" 测试 process"
__author__ = 'AWT'

import multiprocessing

def hello(name):
    if not name:
        print('hello world')
    else:
        print("hello " + name)

p = multiprocessing.Process(target=hello, args=('', ))
p2 = multiprocessing.Process(target=hello, args=('jet', ))
p.start()
p2.start()
p2.join() # Block the calling thread until the process whose join() method is called terminates or until the optional timeout occurs
