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
        base_url = 'http://feedblog.ameba.jp/rss/ameblo/'
        ameba_ids = [
            # QunQun
            'abirumiyuki-qunqun4',
            'yamaokayuka-qunqun4',
            'milky-qunqun',
            'asadamimi-qunqun5',
            'ayaka128love',
            'sakuraiharuka-qunqun5',
            'takanamisakura-qunqun7',
            #LinQ
            'natsu-amano',
            'ayaka-ooba',
            'mayu-kishida',
            'maina-kohinata',
            'yusa-sugimoto',
            'naoko-hara',
            'aya-maikawa',
            'mayu-momosaki',
            'chiaki-yoshikawa',
            'kaede-seto',
            'rana-kaizuki',
            'kokoro-araki',
            'sakura-araki',
            'yuumi-takaki',
            'asaka-sakai',
            'ami-himesaki',
            'kana-fukuyama',
            'ayano-yamaki',
        ]

        for ameba_id in ameba_ids:
            url = base_url + ameba_id
            yield AmebloRssRequest(url)

    def parse(self, response):
        if isinstance(response, AmebloRssResponse):
            for entry in response.entries:
                yield scrapy.http.Request(entry.link, self.parse_entry)

    def parse_entry(self, response):
        images = response.css('.skinArticleBody2 .articleText a img::attr(src)').extract()
        yield AmebloImageItem(image_urls=images)
