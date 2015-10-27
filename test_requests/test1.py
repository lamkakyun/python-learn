#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import requests

url = 'https://github.com/timeline.json'
r = requests.get(url)
print(r.url)
print(r.text)
print(r.content)
print(r.json())