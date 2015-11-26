#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

cookie_file = './baidu.cookie'

cookie_file_handler = open(cookie_file, 'r')
cookie_data = cookie_file_handler.readlines()
# print(cookie_data)
cookie_file_handler.close()

cookie_data_obj = json.loads(cookie_data)
print(cookie_data_obj)


