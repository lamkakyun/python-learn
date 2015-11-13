#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 我先从chrome拿到我百度的cookie，再使用这个cookie访问百度，看看返回什么

import urllib2
import cookielib

url = 'http://www.baidu.com'
cookie_file = './tmp.cookie' # 未登录的cookie 文件
cookie_file = './cookie.txt' # 未登录的cookie 文件
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
headers = {'User-Agent': user_agent}

cookie = cookielib.MozillaCookieJar()
cookie.load(cookie_file, ignore_expires=True, ignore_discard=True)

req = urllib2.Request(url, headers=headers)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

res = opener.open(req)

data = res.readlines()

# print data
tmp_file = 'tmp.html'
tmp_f = open(tmp_file, 'w')
for d in data:
    tmp_f.write(d)
    # print d
tmp_f.close()