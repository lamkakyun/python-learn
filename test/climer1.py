#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 处理cookie,保持cookie

import urllib2
import cookielib

cookie_file = './tmp.cookie'
cookie = cookielib.MozillaCookieJar(cookie_file)

handler = urllib2.HTTPCookieProcessor(cookie)

opener = urllib2.build_opener(handler)

url = 'http://www.baidu.com'

res = opener.open(url)

# ignore_discard的意思是即使cookies将被丢弃也将它保存下来
# ignore_expires的意思是如果在该文件中cookies已经存在，则覆盖原文件写入
cookie.save(ignore_discard=True, ignore_expires=True)
