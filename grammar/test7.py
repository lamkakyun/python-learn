#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# multiprocessing 支持两种进程通讯通道，Queue 和 Pipes
import multiprocessing

def f(s_conn):
    s_conn.send([55, None, 'hello'])
    s_conn.close()

if __name__ == '__main__':
    p_conn, s_conn = multiprocessing.Pipe()
    p = multiprocessing.Process(target=f, args=(s_conn, ))
    p.start()
    print(p_conn.recv())
    p.join()