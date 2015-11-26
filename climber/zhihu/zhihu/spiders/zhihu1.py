# -*- coding: utf-8 -*-
import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import SgmlLinkExtractor
from scrapy.http import Request, FormRequest

class Zhihu1Spider(CrawlSpider):
    name = "zhihu1"
    allowed_domains = ["zhihu.com"]
    start_urls = (
        'http://www.zhihu.com/',
    )
    
    # rules = (
    # )

    # 从知乎站点获取的请求头
    headers = {
        'Accept': '*/*',
        "Accept-Encoding": "gzip, deflate",
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2',
        "Connection": "keep-alive",
        "Content-Type":" application/x-www-form-urlencoded; charset=UTF-8",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36',
        "Referer": "http://www.zhihu.com/",
    }

    def start_requests(self):
        return [Request('http://www.zhihu.com/login/email', meta = {'cookiejar': 1}, callback = self.post_login)]


    def post_login(self, response):
        print 'start login...'
        


