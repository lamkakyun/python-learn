#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import nmap # use python-nmap module

nm = nmap.PortScanner()

nm.scan('127.0.0.1', '22-443')
print(nm.command_line())