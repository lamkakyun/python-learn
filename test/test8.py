#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 求取文件大小

import os
import sys

if len(sys.argv) < 2:
    raise ValueError('参数错误')
    exit(-1)

filename = sys.argv[1]
if os.path.isfile(filename):
    print('file_size: %d' % os.path.getsize(filename))
elif os.path.isdir(filename):
    dirsize = 0
    for dirpath, dirs, files in os.walk(filename):
        for f in files:
            _f = os.path.join(dirpath,f)
            dirsize += os.path.getsize(_f)
    print('dir_size: %d' % dirsize)
else:
    exit(0)
