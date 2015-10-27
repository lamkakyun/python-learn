#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import threading
# local_school看成全局变量，但每个属性如local_school.student都是线程的局部变量，可以任意读写而互不干扰
local_student = threading.local()

def process_student():
    print(local_student)
    print('hello, %s (in %s)' % (local_student.student, threading.current_thread().name))

def process_thread(name):
    local_student.student = name
    process_student()

if __name__ == '__main__':
    t1 = threading.Thread(target=process_thread, args=('jet',))
    t2 = threading.Thread(target=process_thread, args=('tom',))
    t1.start()
    t2.start()