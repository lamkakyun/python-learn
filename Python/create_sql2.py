#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 用来创建SQL文件
# 版本2

sql_file = 'D:/create_sql.sql'
fields = ('url', 'title', 'content')
str_fileds = '('
for field in fields:
    str_fileds += field + ","

str_fileds = str_fileds[:-1]
str_fileds += ')'

f = open(sql_file, 'w')

count = 100
for i in range(1, count + 1):
    url = "http://testwebpy.com/" + str(i)
    title = 'testwebpy title ' + str(i)
    content = '【testwebpy content ' + str(i) + '】'
    content = 5 * content

    str_values = '('
    for field in fields:
        str_values += "'" + eval(field) + "',"
    str_values = str_values[:-1]
    str_values += ');'

    sql = 'insert into pages ' + str_fileds + ' values ' + str_values + '\n'
    f.write(sql)

f.close()
