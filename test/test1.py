#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 备份文件

import shutil
import os

def backUpFile(src, dest):
    return shutil.copytree(src, dest)

if __name__ == "__main__":
    # 备份Coding文件
    backUpFile(os.path.expanduser('~/Coding'), os.path.expanduser('~/Backup'))