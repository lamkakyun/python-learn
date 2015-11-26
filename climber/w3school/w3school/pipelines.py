# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs


# 要调用pipeline， 必须进行配置
class W3SchoolPipeline(object):


    # 定义一个init, 用来指定爬虫数据的保存文件
    def __init__(self):
        self.file = codecs.open('w3school_data_utf8.json', 'wb', encoding='utf-8') # 使用utf-8编码打开文件


    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n' # 对象转为字符串
        self.file.write(line.decode('unicode_escape')) # 将爬虫数据写到文件
        return item # 将爬虫数据返回到输出屏幕
