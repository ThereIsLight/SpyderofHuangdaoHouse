import base64

# 代理服务器
proxyServer = "http://proxy.abuyun.com:9010"

# 代理隧道验证信息
proxyUser = "HP508L18K654WPPP"
proxyPass = "67D075A4D67385B0"

# for Python2
# proxyAuth = "Basic " + base64.b64encode(proxyUser + ":" + proxyPass)
# for Python3
proxyAuth = "Basic " + base64.urlsafe_b64encode(bytes((proxyUser + ":" + proxyPass), "ascii")).decode("utf8")


class ProxyMiddleware(object):

    def process_request(self, request, spider):
        request.meta["proxy"] = proxyServer
        request.headers["Proxy-Authorization"] = proxyAuth