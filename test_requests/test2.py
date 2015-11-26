#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 定制请求头

import requests

url = 'https://api.github.com/some/endpoint'

data = {
    'some': 'data'
}

headers = {
    'content-type': 'application/json'
}

r = requests.post(url, data=data, headers=headers) # post 请求

print(r.content) # 输出请求内容

