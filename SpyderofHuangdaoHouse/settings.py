# -*- coding: utf-8 -*-

# Scrapy settings for SpyderofHuangdaoHouse project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'SpyderofHuangdaoHouse'

SPIDER_MODULES = ['SpyderofHuangdaoHouse.spiders']
NEWSPIDER_MODULE = 'SpyderofHuangdaoHouse.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'SpyderofHuangdaoHouse (+http://www.yourdomain.com)'
USER_AGENTS = [

    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",

    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",

    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",

    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",

    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",

    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",

    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",

    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",

    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",

    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",

    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",

    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",

    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",

    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",

    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",

    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",

    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",

    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",

    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",

    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",

    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",

    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",

    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",

    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",

    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",

    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",

    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",

    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",

    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",

    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",

    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",

    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",

    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",

    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"

]

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'SpyderofHuangdaoHouse.middlewares.SpyderofhuangdaohouseSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
#    'SpyderofHuangdaoHouse.middlewares.MyCustomDownloaderMiddleware': 543,
    'SpyderofHuangdaoHouse.middlewares.random_user_agent.RandomUserAgent': 1,
    # 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
    'SpyderofHuangdaoHouse.middlewares.random_proxy_ip.ProxyMiddleware': 100,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110, #代理需要用到

}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'SpyderofHuangdaoHouse.pipelines.SpyderofhuangdaohousePipeline': 300,
   'SpyderofHuangdaoHouse.lianjia2.pipeline_lianjia2.Lianjia2Pipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# Data Base
MYSQL_HOSTS = '127.0.0.1'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'yg19940916'
MYSQL_PORT = '3306'
MYSQL_DB = 'lianjia2'

#Proxy IP
HTTP_PROXY ='http://127.0.0.1:8123'
#使用Tor
PROXIES =[
{"port": "8998", "ip": "183.147.137.246"},
{"port": "808", "ip": "106.46.136.81"},
{"port": "8118", "ip": "121.204.165.135"},
{"port": "808", "ip": "106.46.136.145"},
{"port": "808", "ip": "221.216.94.77"},
{"port": "808", "ip": "106.46.136.76"},
{"port": "843", "ip": "124.88.67.52"},
{"port": "808", "ip": "106.46.136.87"},
{"port": "808", "ip": "114.239.149.144"},
{"port": "808", "ip": "115.220.6.235"},
{"port": "808", "ip": "123.169.39.23"},
{"port": "80", "ip": "222.37.5.5"},
{"port": "808", "ip": "106.46.136.19"},
{"port": "808", "ip": "106.46.136.171"},
{"port": "9999", "ip": "101.53.101.172"},
{"port": "808", "ip": "106.46.136.142"},
{"port": "808", "ip": "106.46.136.151"},
{"port": "8888", "ip": "180.76.154.5"},
{"port": "808", "ip": "119.5.0.77"},
{"port": "808", "ip": "175.155.24.5"},
{"port": "808", "ip": "106.46.136.130"},
{"port": "808", "ip": "106.46.136.155"},
{"port": "808", "ip": "175.155.25.12"},
{"port": "808", "ip": "119.5.0.70"},
{"port": "808", "ip": "113.69.39.228"},
{"port": "808", "ip": "113.69.63.169"},
{"port": "808", "ip": "115.220.0.192"},
{"port": "808", "ip": "114.230.30.25"},
{"port": "808", "ip": "113.69.62.241"},
{"port": "808", "ip": "113.69.255.145"},
{"port": "80", "ip": "106.120.78.129"},
{"port": "80", "ip": "123.245.83.6"},
{"port": "8118", "ip": "42.196.254.108"},
{"port": "808", "ip": "106.46.136.116"},
{"port": "8998", "ip": "119.0.161.163"},
{"port": "808", "ip": "175.155.155.175"},
{"port": "808", "ip": "171.13.37.54"},
{"port": "808", "ip": "175.155.228.201"},
{"port": "8123", "ip": "171.38.154.45"},
{"port": "808", "ip": "119.5.1.22"},
{"port": "808", "ip": "119.5.0.6"},
{"port": "808", "ip": "106.46.136.172"},
{"port": "8118", "ip": "121.204.165.91"},
{"port": "808", "ip": "183.32.88.136"},
{"port": "808", "ip": "36.249.28.106"},
{"port": "808", "ip": "106.46.136.140"},
{"port": "808", "ip": "114.239.2.180"},
{"port": "808", "ip": "119.5.0.103"},
{"port": "8118", "ip": "222.33.192.238"},
{"port": "808", "ip": "119.5.0.14"},
{"port": "808", "ip": "115.220.147.172"},
{"port": "808", "ip": "114.239.0.250"},
{"port": "808", "ip": "114.230.41.187"},
{"port": "808", "ip": "114.239.3.7"},
{"port": "8080", "ip": "222.90.44.195"},
{"port": "8118", "ip": "101.200.40.179"},
{"port": "808", "ip": "111.72.126.117"},
{"port": "808", "ip": "106.46.136.12"},
{"port": "808", "ip": "183.32.88.132"},
{"port": "808", "ip": "175.155.25.61"},
{"port": "808", "ip": "119.5.0.119"},
{"port": "8118", "ip": "118.123.47.133"},
{"port": "808", "ip": "106.46.136.164"},
{"port": "808", "ip": "175.155.224.110"},
{"port": "8118", "ip": "27.159.126.160"},
{"port": "808", "ip": "106.46.136.175"},
{"port": "808", "ip": "106.46.136.139"},
{"port": "808", "ip": "106.46.136.91"},
{"port": "808", "ip": "119.5.1.48"},
{"port": "808", "ip": "106.46.136.122"},
{"port": "8118", "ip": "125.126.182.217"},
{"port": "808", "ip": "115.220.0.125"},
{"port": "808", "ip": "111.72.126.27"},
{"port": "808", "ip": "171.13.36.242"},
{"port": "808", "ip": "106.46.136.50"},
{"port": "808", "ip": "175.155.25.7"},
{"port": "80", "ip": "115.217.8.210"},
{"port": "808", "ip": "106.46.136.193"},
{"port": "8118", "ip": "121.204.201.182"},
{"port": "808", "ip": "119.5.0.78"},
{"port": "808", "ip": "119.5.0.102"},
{"port": "808", "ip": "114.230.219.152"},
{"port": "808", "ip": "122.5.81.117"},
{"port": "808", "ip": "122.5.80.67"},
{"port": "808", "ip": "106.46.136.123"},
{"port": "808", "ip": "106.46.136.174"},
{"port": "808", "ip": "106.46.136.35"},
{"port": "808", "ip": "180.110.135.101"},
{"port": "808", "ip": "106.46.136.169"},
{"port": "808", "ip": "106.46.136.61"},
{"port": "808", "ip": "175.155.25.32"},
{"port": "80", "ip": "119.90.24.24"},
{"port": "808", "ip": "114.239.2.252"},
{"port": "808", "ip": "183.32.88.91"},
{"port": "808", "ip": "106.46.136.99"},
{"port": "8123", "ip": "121.31.142.153"},
{"port": "808", "ip": "113.58.235.2"},
{"port": "808", "ip": "114.239.146.21"},
{"port": "808", "ip": "113.58.235.194"},
{"port": "1337", "ip": "221.10.159.234"}
]