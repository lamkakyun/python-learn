#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 同步进程，通过Lock类实现
import multiprocessing

def f(l, i):
    l.acquire()
    print('hello world', i) # 确保只有一个进程进入打印
    l.release()

if __name__ == '__main__':
    lock = multiprocessing.Lock()
    for i in range(10):
        multiprocessing.Process(target=f, args=(lock, i)).start()