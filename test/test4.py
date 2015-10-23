#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 判断目录之下是否有sqlite3文件

import sys
import os

def is_sqlite(file):
    if not os.path.isfile(file):return False
    if os.path.getsize(file) < 100: return False
    else:
        f = open(file, 'r')
        header = f.read(100) # read 100 bytes
        return True if header[0:16] == 'SQLite format 3\000' else False

if __name__ == "__main__":

    check_dir = os.path.expanduser('~') if len(sys.argv) < 2 else sys.argv[1]

    if not os.path.isdir(check_dir):
        print(check_dir + ' is not a dir')
        exit(1)

    _sqlite_files = []
    for dirpath, dirnames, filenames in os.walk(check_dir):
        for file in filenames:
            if is_sqlite(file):
                print('find a sqlite file:' + os.path.join(dirpath, file))
                _sqlite_files.append(os.path.join(dirpath, file))

    if len(_sqlite_files) == 0:
        print('no sqlite file')
    else: print(_sqlite_files)
