#!/usr/bin/evn python
# -*- coding: UTF-8 -*-
# 从文件中读取数据

import os
import sys

def readfile(file):
    with open(file, 'r') as f:
        print(f.read())

def main():
    if len(sys.argv) == 2:
        if not os.path.isfile(sys.argv[1]):
            print(sys.argv[1] + 'not a file')
            exit(0)
        elif not os.access(sys.argv[1], os.R_OK):
            print(sys.argv[1] + 'is access denied')
            exit(0)
    else:
        print('arguments count error')
        exit(0)

    print('read from ' + sys.argv[1])
    readfile(sys.argv[1])

if __name__ == "__main__":
    main()