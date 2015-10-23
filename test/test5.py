#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 遍历目录

import os
import sys

if __name__ == '__main__':
    dir = os.path.expanduser('~') if len(sys.argv) < 2 else sys.argv[1]

    if not os.path.isdir(dir):
        print(dir + ' is not a dir')
        exit(1)

    for dirpath, dirs, files in os.walk(dir):
        print( dirpath)
        print(dirs)
        print(files)

