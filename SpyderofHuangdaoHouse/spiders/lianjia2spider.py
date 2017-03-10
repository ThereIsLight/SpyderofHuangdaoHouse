import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request #一个单独的request模块，需要跟进的url时，能够用到它
from SpyderofHuangdaoHouse.items import Lianjia2Item
import re
import json
import logging
# from scrapy import log  #Module `scrapy.log` has been deprecated, Scrapy now relies on the builtin Python library for logging.


class Lianjia2Spider(scrapy.Spider):

    name = "lianjia2"
    allowed_domains = ["qd.lianjia.com"]
    head_url = "http://qd.lianjia.com/ershoufang/huangdao/"
    com_url = "http://qd.lianjia.com"
    count = 0
    logger = logging.getLogger()

    def start_requests(self):
        start_url = self.head_url
        yield Request(start_url, self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        dict_str = soup.find('div', class_="page-box house-lst-page-box")['page-data']  #get str like {"totalPage":61,"curPage":1}
        max_page = json.loads(dict_str)['totalPage']  #switch str to dict

        for i in range(1, int(max_page) + 1):
            url = self.head_url + "pg" + str(i)
            yield Request(url, callback=self.get_link)

    def get_link(self, response):

        lis = BeautifulSoup(response.text, "lxml").find('ul', class_='sellListContent').find_all('li', class_="clear")
        for li in lis:
            link = li.find('a', class_="img")['href']
            yield Request(link, callback=self.get_info)

    def get_info(self, response):

        soup = BeautifulSoup(response.text, 'lxml')
        item = Lianjia2Item()

        name = soup.find('div', class_='sellDetailHeader').find('div', class_='title').find('h1').get_text()
        price = soup.find('div', class_="price").find('span', class_='total').get_text()  #单位是万元
        temp_aver = soup.find('div', class_="unitPrice").find('span', class_='unitPriceValue').get_text()  #单位是元
        aver = re.findall(r"\d+", temp_aver)[0]
        temp_build_time = soup.find('div', 'subInfo').get_text()
        build_time = re.findall(r'\d+', temp_build_time)[0]  #将list转化为字符串
        subdistrict = soup.find('div', class_='areaName').find('span', class_='info').find_all('a')[1].get_text()
        community = soup.find('div', class_='communityName').find('a', class_='info').get_text()
        source = '链家'
        link = response.url  # maybe this function
        area = soup.find('div', class_='base').find('div', 'content').find_all('li')[2].contents[-1].strip()
        house_type = soup.find('div', class_='base').find('div', 'content').find_all('li')[0].contents[-1].strip()
        floor = soup.find('div', class_='base').find('div', 'content').find_all('li')[1].contents[-1].strip()
        decoration = soup.find('div', class_='base').find('div', 'content').find_all('li')[8].contents[-1].strip()
        orientation = soup.find('div', class_='base').find('div', 'content').find_all('li')[6].contents[-1].strip()
        build_type = soup.find('div', class_='base').find('div', 'content').find_all('li')[5].contents[-1].strip()
        structure = soup.find('div', class_='base').find('div', 'content').find_all('li')[7].contents[-1].strip()
        use = soup.find('div', class_='transaction').find('div', 'content').find_all('li')[3].contents[-1].strip()

        item['name'] = name
        item['price'] = float(price)
        item['aver'] = float(aver)
        item['build_time'] = float(build_time)
        item['subdistrict'] = subdistrict
        item['community'] = community
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


