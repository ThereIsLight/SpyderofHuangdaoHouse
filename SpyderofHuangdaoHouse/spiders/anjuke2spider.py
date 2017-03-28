from SpyderofHuangdaoHouse.items import ResoldHouseItem
import scrapy
from scrapy.http import Request
import re
import logging

"""
安居客二手房爬虫：
运行前需要看的注意事项：
0.安居客的网站突然抽风，不知道为什么，二手房网页无法访问。
1.安居客新房网站总共51个索引网页。但是找不到最后一页具体的数字。而且数字可能会发生改变。
2.在具体信息界面中的各种信息的位置是固定的。喜大普蹦！！
3.每次运行爬虫之前，都要修改settings.py与run_spider.py中的数据。
4.最终运行之前要修改sql_anjuke2中表与数据库的名字
5.将代码修改为爬取全部的数据

2017年3月27日10:43:49
第一次运行爬虫：运行成功，插入一条数据。但是多次运行之后，返回二手房界面为404 not find。

2017年3月28日09:39:20
到目前为止安居客二手房的网页一直无法打开。为什么？？网站抽风了。。。
"""


class Anjuke2Spider(scrapy.Spider):

    name = 'anjuke2'
    allowed_domains = ['qd.anjuke.com']
    head_url = 'https://qd.anjuke.com/sale/huangdaoqu/'

    logger = logging.getLogger()

    def start_requests(self):
        for i in range(1, 51):  #在页面中找不到最后一页，只能用现成的数字。
        # for i in range(1, 2):  # test
            page_url = self.head_url + 'p' + str(i)
            yield Request(page_url)

    def parse(self, response):
        """
        lis = response.xpath('//*[@id="houselist-mod"]/li')
        for li in lis:
            info_url = li.xpath("div[2]/div[1]/a/@href").extract()[0]  # /只能选取当前结点的子节点，不能选择孙节点。
            print(info_url)
            # yield Request(info_url, callback=self.get_info)
        """
        li = response.xpath('//*[@id="houselist-mod"]/li')
        info_url = li.xpath("div[2]/div[1]/a/@href").extract()[0]
        # print(info_url)
        yield Request(info_url, callback=self.get_info)

    def get_info(self, response):
        """
        貌似安居客二手房的信息格式是固定的，喜大普奔啊
        :param response:
        :return:
        """
        re_num = re.compile(r"\d+\.?\d*")
        item = ResoldHouseItem()

        name = response.xpath('//*[@id="content"]/div[2]/h3/text()').extract()[0].strip()
        price = response.xpath('//*[@id="content"]/div[3]/div[1]/div[1]/span[1]/em/text()').extract()[0]  # 直接获得了数字，不需要正则表达式。
        aver = response.xpath('//*[@id="content"]/div[3]/div[1]/div[3]/div/div/div[1]/div[3]/dl[2]/dd/text()').extract()[0]  # 需要使用正则表达式提取数字
        aver = re.findall(re_num, aver)[0]
        build_time = response.xpath('//*[@id="content"]/div[3]/div[1]/div[3]/div/div/div[1]/div[1]/dl[3]/dd/text()').extract()[0]
        build_time = re.findall(re_num, build_time)[0]
        subdistrict = response.xpath('//*[@id="content"]/div[3]/div[1]/div[3]/div/div/div[1]/div[1]/dl[2]/dd/p/a[2]/text()').extract()[0]
        community = response.xpath('//*[@id="content"]/div[3]/div[1]/div[3]/div/div/div[1]/div[1]/dl[1]/dd/a/text()').extract()[0]
        address = response.xpath('//*[@id="content"]/div[3]/div[1]/div[3]/div/div/div[1]/div[1]/dl[2]/dd/p/text()[2]').extract()[0]  # 格式为"-   XXX"
        address = (''.join(address.split()))  # 先去掉空白符，将格式变为"-XXXX"
        address = address.strip('－')  # ,再去掉开头的'－'，注意这里不是减号，而是汉字中的破折号。
        source = '安居客'
        link = response.url  # maybe this function
        area = response.xpath('//*[@id="content"]/div[3]/div[1]/div[1]/span[3]/em/text()').extract()[0]  # 不需要提取数字
        house_type = response.xpath('//*[@id="content"]/div[3]/div[1]/div[3]/div/div/div[1]/div[2]/dl[1]/dd/text()').extract()[0]  # 字符串的前后，中间都有空白符。
        house_type = " ".join(house_type.split())
        floor = response.xpath('//*[@id="content"]/div[3]/div[1]/div[3]/div/div/div[1]/div[2]/dl[4]/dd/text()').extract()[0].strip()  # 后面有一段空白
        decoration = response.xpath('//*[@id="content"]/div[3]/div[1]/div[3]/div/div/div[1]/div[3]/dl[1]/dd/text()').extract()[0]
        orientation = response.xpath('//*[@id="content"]/div[3]/div[1]/div[3]/div/div/div[1]/div[2]/dl[3]/dd/text()').extract()[0]
        build_type = '没有数据'
        structure = '没有数据'
        use = response.xpath('//*[@id="content"]/div[3]/div[1]/div[3]/div/div/div[1]/div[1]/dl[4]/dd/text()').extract()[0]
        '''
        print('name', name)
        print('price', price)
        print('aver', aver)
        print('build_time', build_time)
        print('subdistrict', subdistrict)
        print('community', community)
        print('address', address)
        print('source', source)
        print('link', link)
        print('area', area)
        print('house_type', house_type)
        print('floor', floor)
        print('decoration', decoration)
        print('orientation', orientation)
        print('build_type', build_type)
        print('structure', structure)
        print('use', use)
        '''
        item['name'] = name
        item['price'] = float(price)
        item['aver'] = float(aver)
        item['build_time'] = float(build_time)
        item['subdistrict'] = subdistrict
        item['community'] = community
        item['address'] = address
        item['source'] = source
        item['link'] = link
        item['area'] = float(area.strip('㎡'))
        item['house_type'] = house_type
        item['floor'] = floor
        item['decoration'] = decoration
        item['orientation'] = orientation
        item['build_type'] = build_type
        item['structure'] = structure
        item['use'] = use
        # self.logger.info(item)
        yield item
