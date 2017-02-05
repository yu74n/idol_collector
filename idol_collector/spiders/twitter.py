# -*- coding: utf-8 -*-
import scrapy


class TwitterSpider(scrapy.Spider):
    name = "twitter"
    allowed_domains = ["api.twitter.com"]
    #start_urls = ['http://api.twitter.com/']

    def start_requests(self):
        pass

    def parse(self, response):
        pass
