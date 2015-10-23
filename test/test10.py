#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 修改时间超过240天，自动移动到新的目录

import os
import shutil

srcdir = "/home/jet/Documents"
destdir = "/media/jet/BackupDisk"

if os.path.exists(destdir):
    raise ValueError("目标目录不存在")
    exit(-1)

now = time.time()

for f in os.listdir(srcdir):
    if now - 240 * 24 * 60 * 60 > os.stat(f).st_mtime:
        if os.path.isfile(f):
            shutil.move(f, destdir)