# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 如果您仅仅想要保存item，您不需要实现任何的pipeline。
# 如果需要对爬取到的item做更多更为复杂的操作，您可以编写 Item Pipeline

class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item
