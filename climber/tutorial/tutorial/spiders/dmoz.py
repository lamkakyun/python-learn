# -*- coding: utf-8 -*-
import scrapy

# 导入Item
from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
#    start_urls = (
#        'http://www.dmoz.org/',
#    )
    
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]


    # 将会获取上面两个链接的网页内容，并保存到第二级目录
#    def parse(self, response):
#        filename =  response.url.split('/')[-2]
#        with open(filename, 'wb') as f:
#            f.write(response.body)

# scrapy shell "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/"
# response.xpath('//title') # 获得selector对象
# response.xpath('//title').extract() # 获得title 元素内容
# response.xpath('//title/text()').extract()
# response.xpath('//title/text()').re('(\w+):')

    # 由以上知识，重写方法
#    def parse(self, response):
#        for selector in response.xpath('//ul/li'):
#            title = selector.xpath('a/text()').extract()
#            link = selector.xpath('a/@href').extract()
#            desc = selector.xpath('text()').extract()
#            print title, link, desc
        

    # 使用css重新实现
#    def parse(self, response):
#        for selector in response.css('ul>li'):
#            title = selector.css('a::text').extract()
#            link = selector.css('a::attr(href)').extract()
#            desc = selector.css('::text').extract()
#            print title, link, desc

    # 一般来说，Spider将会将爬取到的数据以 Item 对象返回,所以要这样实现
    # 可以通过，scrapy crawl dmoz -o items.json, 保存成文件
    def parse(self, response):
        for selector in response.xpath('//ul/li'):
            item = DmozItem() 
            item['title'] = selector.xpath('a/text()').extract()
            item['link'] = selector.xpath('a/@href').extract()
            item['desc'] = selector.xpath('text()').extract()
            yield item
