#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import cookielib

file_name = 'tmp_cookie.txt'
cookie = cookielib.MozillaCookieJar(file_name)

handler = urllib2.HTTPCookieProcessor(cookie)

opener = urllib2.build_opener(handler)

url = 'http://www.baidu.com'

res = opener.open(url)

print(res.readlines())

cookie.save(ignore_discard=True, ignore_expires=True)


