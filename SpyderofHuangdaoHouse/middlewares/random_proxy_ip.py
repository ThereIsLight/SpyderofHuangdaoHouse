import random
# from SpyderofHuangdaoHouse.settings import HTTP_PROXY
from SpyderofHuangdaoHouse.settings import PROXIES

class ProxyMiddleware(object):

    def process_request(self, request, spider):
        # print(HTTP_PROXY)
        # request.meta['proxy'] = HTTP_PROXY
        proxy = random.choice(PROXIES)
        print("http://%s" % (proxy['ip'] + ':' + proxy['port']))
        request.meta['proxy'] = "http://%s" % (proxy['ip'] + ':' + proxy['port'])