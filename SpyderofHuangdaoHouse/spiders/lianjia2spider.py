import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request #一个单独的request模块，需要跟进的url时，能够用到它
from SpyderofHuangdaoHouse.items import ResoldHouseItem
import re
import json
import logging
"""
链家二手房爬虫：
运行前需要看的注意事项：
1.每次运行爬虫之前，都要修改settings.py与run_spider.py中的数据。
2.最终运行之前要修改sql_了；lianjia2中表与数据库的名字
"""
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
        # for i in range(1, 2):
            url = self.head_url + "pg" + str(i)
            yield Request(url, callback=self.get_link)

    def get_link(self, response):

        lis = BeautifulSoup(response.text, "lxml").find('ul', class_='sellListContent').find_all('li', class_="clear")
        for li in lis:
            info_url = li.find('a', class_="img")['href']
            print(info_url)
            yield Request(info_url, callback=self.get_info)
        '''
        li = BeautifulSoup(response.text, "lxml").find('ul', class_='sellListContent').find('li', class_="clear")
        info_url = li.find('a', class_="img")['href']
        yield Request(info_url, callback=self.get_info)
        '''
    def get_info(self, response):
        """
        这里的网页结构分为两种格式，一种是别墅，另一种非别墅。别墅界面会缺少少量的数据。
        按照网页类型将字段分为三种格式：固定属性，基本属性，交易属性。其中固定属性以及交易属性的位置是固定的(目前是固定的)。基本属性的位置不是固定的。
        固定属性：name,price,aver,build_time,subdistrict,community,area,(house_type,floor,decoration,orientation)(在基本属性中但是位置是固定的)
        基本属性：build_type(别墅没有建筑类别) structure(两类网页位置不一致)
        交易属性：use 位置固定。
        :param response:
        :return:
        """
        soup = BeautifulSoup(response.text, 'lxml')
        item = ResoldHouseItem()
        re_num = re.compile(r"\d+\.?\d*")

        name = soup.find('div', class_='sellDetailHeader').find('div', class_='title').find('h1').get_text()
        price = soup.find('div', class_="price").find('span', class_='total').get_text()  #单位是万元
        temp_aver = soup.find('div', class_="unitPrice").find('span', class_='unitPriceValue').get_text()  #单位是元
        aver = re.findall(re_num, temp_aver)[0]
        build_time = soup.find('div', class_='houseInfo').find('div', class_='area').find('div', 'subInfo').get_text()
        build_time = re.findall(re_num, build_time)  # 将list转化为字符串，但是某些网页没有年份。
        if build_time:
            build_time = float(build_time[0])
        else:
            build_time = 0
        subdistrict = soup.find('div', class_='areaName').find('span', class_='info').find_all('a')[1].get_text()
        address = '暂无数据'
        community = soup.find('div', class_='communityName').find('a', class_='info').get_text()
        source = '链家'
        link = response.url  # maybe this function
        area = soup.find('div', class_='base').find('div', 'content').find_all('li')[2].contents[-1].strip()

        # 在两类网页中位置一样，但是需要重新写代码
        house_type = soup.find('div', class_='base').find('div', 'content').find_all('li')[0].contents[-1].strip()
        floor = soup.find('div', class_='base').find('div', 'content').find_all('li')[1].contents[-1].strip()
        decoration = soup.find('div', class_='houseInfo').find('div', class_='type').find('div', class_='subInfo').get_text()
        orientation = soup.find('div', class_='houseInfo').find('div', class_='type').find('div', class_='mainInfo').get_text()
        use = soup.find('div', class_='transaction').find('div', 'content').find_all('li')[3].contents[-1].strip()
        # 在两类网页中位置不一样
        if use == '别墅':
            build_type = "暂无数据"
            structure = soup.find('div', class_='base').find('div', 'content').find_all('li')[5].contents[-1].strip()
        else:
            build_type = soup.find('div', class_='base').find('div', 'content').find_all('li')[5].contents[-1].strip()
            structure = soup.find('div', class_='base').find('div', 'content').find_all('li')[7].contents[-1].strip()
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
        item['build_time'] = build_time
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



