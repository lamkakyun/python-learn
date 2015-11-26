# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

HOST = '127.0.0.1'
PORT = 27017

class Tech163Pipeline(object):
    def process_item(self, item, spider):
        # if spider.name != 'tech': return item # 非tech spider，直接返回，否则保存到mongodb

        client = pymongo.MongoClient(HOST, PORT)

        db = client.jetdb

        # 请参考pymongo使用
        db.news.insert_one(dict(item))

        return None


