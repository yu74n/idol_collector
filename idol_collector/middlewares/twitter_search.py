import logging
from twitter import Twitter, OAuth
from scrapy.http import Request, Response

logger = logging.getLogger(__name__)

class TwitterSearchRequest(Request):
    def __init__(self, *args, **kwargs):
        self.keyword = kwargs.pop('keyword', None)
        super(TwitterSearchRequest, self).__init__(*args, **kwargs)

class TwitterSearchResponse(Response):
    def __init__(self, *args, **kwargs):
        self.result = kwargs.pop('result', None)
        super(TwitterSearchResponse, self).__init__(*args, **kwargs)

class TwitterSearchMiddleware(object):
    def __init__(self, access_token, access_secret, consumer_key, consumer_secret):
        self.access_token = access_token
        self.access_secret = access_secret
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.get('TWITTER_API_ACCESS_TOKEN'),\
                crawler.settings.get('TWITTER_API_ACCESS_TOKEN_SECRET'),\
                crawler.settings.get('TWITTER_API_CONSUMER_KEY'),\
                crawler.settings.get('TWITTER_API_CONSUMER_SECRET'))

    def process_request(self, request, spider):
        if isinstance(request, TwitterSearchRequest):
            t = Twitter(auth=OAuth(self.access_token, \
                    self.access_secret, \
                    self.consumer_key, \
                    self.consumer_secret))
            result = t.statuses.user_timeline(screen_name=request.keyword)
            return TwitterSearchResponse(request.url, result=result)
