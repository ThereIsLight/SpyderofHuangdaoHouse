import base64

# 代理服务器
proxyServer = "http://proxy.abuyun.com:9020"

# 代理隧道验证信息
proxyUser = "H2F3OT1C316O0T3D"
proxyPass = "B33C81A6D80B6EB7"

# for Python2
# proxyAuth = "Basic " + base64.b64encode(proxyUser + ":" + proxyPass)
# for Python3
proxyAuth = "Basic " + base64.urlsafe_b64encode(bytes((proxyUser + ":" + proxyPass), "ascii")).decode("utf8")


class ProxyMiddleware(object):

    def process_request(self, request, spider):
        request.meta["proxy"] = proxyServer
        request.headers["Proxy-Authorization"] = proxyAuth