import feedparser
import logging
import scrapy

logger = logging.getLogger(__name__)

class AmebloRssRequest(scrapy.Request):
    def __init__(self, *args, **kwargs):
        self.ameba_id = kwargs.pop('ameba_id', None)
        super(AmebloRssRequest, self).__init__(*args, **kwargs)

class AmebloRssResponse(scrapy.http.Response):
    def __init__(self, *args, **kwargs):
        self.entries = kwargs.pop('entries', [])
        super(AmebloRssResponse, self).__init__(*args, **kwargs)

class AmebloRssMiddleware(object):
    RSS_BASEURL = 'http://feedblog.ameba.jp/rss/ameblo/'

    def process_request(self, request, spider):
        if isinstance(request, AmebloRssRequest):
            url = self.RSS_BASEURL + request.ameba_id
            logger.info(url)
            response = feedparser.parse(url)
            return AmebloRssResponse(request.url, entries=response.entries)
