#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 批量更新扩展名

import sys
import os

if len(sys.argv) != 4:
    raise ValueError('参数错误，需要3个参数')

renameDir = os.path.expanduser(sys.argv[1])
oldExt = sys.argv[2]
newExt = sys.argv[3]

if (os.path.isdir(renameDir) == False):
    raise ValueError(renameDir + ' is not a dir')

for fileName in os.listdir(renameDir):
    if (os.path.isfile(fileName)):
        if (fileName.endswith(newExt)):
            continue

        old_file_name = os.path.join(renameDir, fileName)
        _file_name = os.path.splitext(fileName)
        new_file_name = os.path.join(renameDir, (_file_name[0] + newExt))
        os.rename(old_file_name, new_file_name)