#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 打印系统系统

import platform

profile =  [
    platform.architecture(),
    platform.dist(), # 发行版
    platform.libc_ver(),
    platform.mac_ver(), # mac os info
    platform.node(), # computer network name
    platform.platform(),
    platform.processor(),
    platform.python_build(),
    platform.python_compiler(),
    platform.python_version(),
    platform.release(),
    platform.system(),
    platform.uname(),
    platform.version()
]

i = 1
for item in profile:
    print('#', i, ' ', item)
    i += 1