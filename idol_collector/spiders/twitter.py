# -*- coding: utf-8 -*-
import json
import scrapy
from idol_collector.middlewares.twitter_search import TwitterSearchRequest
from idol_collector.items import TwitterImageItem

class TwitterSpider(scrapy.Spider):
    name = "twitter"
    allowed_domains = ["api.twitter.com"]

    def start_requests(self):
        yield TwitterSearchRequest('http://api.twitter.com', self.parse, keyword='yuka_qun4')

    def parse(self, response):
        entries = response.result
        image_urls = []
        for entry in entries:
            if 'extended_entities' in entry:
                if 'media' in entry['extended_entities']:
                    for item in entry['entities']['media']:
                        url = item['media_url']
                        image_urls.append(url)
        yield TwitterImageItem(image_urls=image_urls)

        with open('twitter_yuka3.jl', 'ab') as fp:
            encoded = json.dumps(entries).encode('utf-8')
            fp.write(encoded)
