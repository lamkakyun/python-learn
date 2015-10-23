#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 在进程之间分享状态,使用multiprocess 的sharedtype
import  multiprocessing

def f(num, arr):
    num.value = 3.1415927
    for i in range(len(arr)):
        arr[i] = -arr[i]

if __name__ == '__main__':
    num = multiprocessing.Value('d', 0.0) # return double type
    arr = multiprocessing.Array('i', range(10)) # return int array

    p = multiprocessing.Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])
