# -*- coding: utf-8 -*-
import scrapy

from w3school.items import  W3SchoolItem

class W3spiderSpider(scrapy.Spider):
    name = "w3spider"
    allowed_domains = ["w3school.com.cn"]
    start_urls = [
       'http://www.w3school.com.cn/xml/xml_syntax.asp' 
    ]

    def parse(self, response):
        selectors = response.xpath('//div[@id="navsecond"]/div[@id="course"]/ul[1]/li')
        items = []
        for s in selectors:
            item = W3SchoolItem()

            title = s.xpath('a/text()').extract()
            link = s.xpath('a/@href').extract()
            desc = s.xpath('a/@title').extract()

            # item['title'] = [t.encode('utf-8') for t in title]
            # item['link'] = [l.encode('utf-8') for l in link]
            # item['desc'] = [d.encode('utf-8') for d in desc]

            item['title'] = title
            item['link'] = link
            item['desc'] = desc

            items.append(item)


        return items


    def parse_test(self, response):
        selectors = response.xpath('//div[@id="navsecond"]/div[@id="course"]/ul[1]/li')
        print selectors
        pass
