# -*- coding: utf-8 -*-
import scrapy
import json
import logging
from idol_collector.middlewares.ameblo_rss import AmebloRssRequest, AmebloRssResponse
from idol_collector.items import AmebloImageItem

logger = logging.getLogger(__name__)

class AmebloSpider(scrapy.Spider):
    name = "ameblo"
    allowed_domains = ["feedblog.ameba.jp", "ameblo.jp"]

    def start_requests(self):
        yield AmebloRssRequest('http://feedblog.ameba.jp', self.parse, ameba_id='yamaokayuka-qunqun4')

    def parse(self, response):
        if isinstance(response, AmebloRssResponse):
            for entry in response.entries:
                yield scrapy.http.Request(entry.link, self.parse_entry)

    def parse_entry(self, response):
        images = response.css('.skinArticleBody2 a img::attr(src)').extract()
        yield AmebloImageItem(image_urls=images)
