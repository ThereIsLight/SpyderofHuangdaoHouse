import random

class RandomUserAgent(object):

    def __init__(self, agents):
        """
        :param agent:
        """
        self.agents = agents
    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))  #返回的是本类的实例

    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', random.choice(self.agents))