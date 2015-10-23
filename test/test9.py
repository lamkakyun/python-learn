#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 保存压缩日志文件，并且删除日志文件（网管会用到这个程序）

import os
import time

log_dir = "/var/log"

for f in os.listdir(log_dir):
    if f.endswith('.log'):
        zipfile = f + '.' + time.strftime("%Y-%m-%d") + '.zip'
        os.chdir(log_dir)
        os.system('zip -r %s %s' % (zipfile, f))
        os.remove(f)