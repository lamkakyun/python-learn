#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import multiprocessing
# multiprocessing 支持两种进程通讯通道，Queue 和 Pipes

def f(q):
    q.put([44,None, 'hello'])

if __name__ == '__main__':
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=f, args=(q,))
    p.start()
    print(q.get())
    p.join()