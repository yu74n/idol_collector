import feedparser
import logging
import scrapy

logger = logging.getLogger(__name__)

class AmebloRssRequest(scrapy.Request):
    def __init__(self, *args, **kwargs):
        super(AmebloRssRequest, self).__init__(*args, **kwargs)

class AmebloRssResponse(scrapy.http.Response):
    def __init__(self, *args, **kwargs):
        self.entries = kwargs.pop('entries', [])
        super(AmebloRssResponse, self).__init__(*args, **kwargs)

class AmebloRssMiddleware(object):

    def process_request(self, request, spider):
        if isinstance(request, AmebloRssRequest):
            logger.info(request.url)
            response = feedparser.parse(request.url)
            return AmebloRssResponse(request.url, entries=response.entries)
