#!/usr/bin/evn python
# -*- coding: UTF-8 -*-

import multiprocessing
# 进程学习
# pool() 进程池

import time
import os

def mypow(x):
    print(os.getpid(), os.getppid())
    time.sleep(5) # 5 seconds
    print(x**2)

p = multiprocessing.Pool(5)
p.map(mypow, [1,2,3,4,5,6,7,8,9])
