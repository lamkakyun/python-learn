#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 用来创建SQL文件
# 版本1

import random
import time

f = open('D:\\cost.sql', 'w')
for i in range(1, 1001):
    num = random.randint(1,1000)
    unit_price = round(random.uniform(1,1000), 2)
    total_price = round(num * unit_price, 2)
    create_time = time.strftime('%Y-%m-%d %H:%M:%S')
    create_by_id = random.randint(1,20)
    activites_id = random.randint(1,10)


    sql = "insert into finance_cost_records (name, num, unit_price, total_price, create_time, create_by_id, activites_id) values ('{name}', {num}, {unit_price}, {total_price}, '{create_time}', {create_by_id}, {activites_id});\n".format(name = 'cost_name_' + str(i), num=num, unit_price=unit_price, total_price=total_price, create_time=create_time, create_by_id=create_by_id, activites_id=activites_id)

    f.write(sql)

f.close()
