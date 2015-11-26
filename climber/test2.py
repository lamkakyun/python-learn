#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import cookielib

cookie_file = './cookie.txt'
# cookie_file = './tmp_cookie.txt'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'}

cookie = cookielib.MozillaCookieJar()

cookie.load(cookie_file, ignore_discard=True, ignore_expires=True)

handler = urllib2.HTTPCookieProcessor(cookie)


opener = urllib2.build_opener(handler)

# url = 'http://cn.bing.com'
url = 'http://www.baidu.com'

req = urllib2.Request(url, headers=headers)

res = opener.open(req)

print(res.readlines())

cookie.save('./cookie2.txt')