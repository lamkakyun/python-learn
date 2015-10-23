#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 打印文件信息
import os
import stat
import time

# file_name = raw_input('please input a file name:')
file_name = 'test6.py'
file_stat = os.stat(file_name)

file_info = {
    'fname': file_name,
    'fsize': file_stat[stat.ST_SIZE],
    'fmtime': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(file_stat[stat.ST_MTIME])),
    'fatime': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(file_stat[stat.ST_ATIME])),
    'fctime': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(file_stat[stat.ST_CTIME]))
}

print

print("file name = %(fname)s" % file_info)

if stat.S_ISDIR(file_stat[stat.ST_MODE]):
    print('this is a dir')
else:
    print('is not a dir')

print(file_stat)