#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 使用进程池
import multiprocessing

def f(x):
    return x * x

if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=4)
    result = pool.apply_async(f, [10]) # 异步执行并返回结果
    print(result.get(timeout=1))
    print(pool.map(f, range(10)))
