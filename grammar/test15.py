#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import threading
import multiprocessing

balance = 0
lock = multiprocessing.Lock()

def change_it(n):
    global balance
    balance += n
    balance -= n

def run_thread(n):
    for i in range(100000):
        change_it(n)

def run_thread2(n):
    for i in range(100000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

if __name__ == '__main__':
    t1 = threading.Thread(target=run_thread2, args=(5, ), name='t1')
    t2 = threading.Thread(target=run_thread2, args=(8, ), name='t2')
    t1.start()
    t2.start()
    t1.join() # 线程交叉运行
    t2.join()
    print(balance)