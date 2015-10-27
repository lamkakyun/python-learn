#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#  进程和异常
import multiprocessing
import time
import signal

p = multiprocessing.Process(target=time.sleep, args=(1000,))
print(p, p.is_alive())
p.start()
print(p, p.is_alive())
p.terminate()
time.sleep(0.1)
print(p, p.is_alive())
print(p.exitcode == -signal.SIGTERM)
