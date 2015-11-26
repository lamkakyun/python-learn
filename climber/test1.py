#!/usr/bin/env python
# -*- coding: utf-8 -*-

<<<<<<< HEAD
import urllib2
import cookielib

file_name = 'tmp_cookie.txt'
cookie = cookielib.MozillaCookieJar(file_name)

=======
# 做一个简单的爬虫，爬去plan.l**n.com 站点的数据

import re
import urllib
import urllib2
import cookielib

cookie = cookielib.MozillaCookieJar()
>>>>>>> 590f8bd5ed109ecfa6e949c7697189916d6d1d35
handler = urllib2.HTTPCookieProcessor(cookie)

opener = urllib2.build_opener(handler)

<<<<<<< HEAD
url = 'http://www.baidu.com'

res = opener.open(url)

print(res.readlines())

cookie.save(ignore_discard=True, ignore_expires=True)

=======
login_url = 'https://plan.l***n.com/****'
page_url = 'https://plan.l***n.com/****'

email = '**'
password = '**'
login_data = {'email': email, 'password': password}
req = urllib2.Request(login_url, urllib.urlencode(login_data))

res = opener.open(req)

if res.code != 200:
    raise urllib2.HTTPError(login_url, res.code, '登录失败')

req2 = urllib2.Request(page_url)
res2 = opener.open(req2)

page_data = res2.readlines()

for d in page_data:
    matches = re.findall('<a.*?class="*ite*".*?>(.*?)</a>', d, re.M)
    for m in matches:
        print m
>>>>>>> 590f8bd5ed109ecfa6e949c7697189916d6d1d35

