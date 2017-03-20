import random
from SpyderofHuangdaoHouse.settings import http_proxy

class ProxyMiddleware(object):

    def process_request(self, request, spider):

        proxy = random.choice(http_proxy)
        print("http://%s" % (proxy['ip'] + ':' + proxy['port']))
        request.meta['proxy'] = "http://%s" % (proxy['ip'] + ':' + proxy['port'])