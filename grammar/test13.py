#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import multiprocessing
import os, time, random

def long_time_task(name):
    print('run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('task %s runs %.2f seconds' % (name, (end - start)))

if __name__ == '__main__':
    print('Parent process %s' % os.getpid())
    p = multiprocessing.Pool()
    for i in range(15):
        p.apply_async(long_time_task, args=('__' + str(i), ))
    print('waiting for all subprocess done')
    p.close() # Pool 不能在添加process，必须在join之前调用
    p.join()
    print('all subprocess done')