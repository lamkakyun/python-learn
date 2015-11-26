# -*- coding: utf-8 -*-
import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from tech163.items import ArticleItem


class TechSpider(CrawlSpider):
    name = "tech"
    allowed_domains = ["tech.163.com"]
    start_urls = (
        'http://tech.163.com/',
    )

    # 查询2015年11月的新闻
    rules = (
            Rule(LinkExtractor(allow=r"/15/11\d+/\d+/*"), callback = 'parse_news'),
            )

    # def parse(self, response):
    #     pass

    def parse_news(self, response):
        article = ArticleItem()

        article['title'] = response.css('#h1title::text').extract()[0]
        article['link'] = response.url
        article['content'] = response.css('#endText').extract()[0]

        return article

        # print article['title'][0]
        # print article['content'][0]
        # print response.url
