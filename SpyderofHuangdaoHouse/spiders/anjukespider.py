import scrapy
from scrapy.http import Request
from bs4 import BeautifulSoup
import re
import logging
from SpyderofHuangdaoHouse.items import NewHouseItem

"""
安居客新房爬虫
运行前需要看的注意事项：
1.安居客新房网站总共6个索引网页。但是找不到最后一页具体的数字。
2.在具体信息界面中的各种信息的位置不是固定的。
3.每次运行爬虫之前，都要修改settings.py与run_spider.py中的数据。
4.最终运行之前要修改sql_anjuke2中表与数据库的名字

2017年3月26日11:20:16：
第一次运行：顺利插入一条数据到MySQL数据库中。
出现的问题：sql语句中括号，引号等不匹配。
"""


class AnjukeSpider(scrapy.Spider):

    name = 'anjuke'
    allowed_domains = ['qd.fang.anjuke.com']
    head_url = 'https://qd.fang.anjuke.com/loupan/huangdaoqu/'

    logger = logging.getLogger()

    def start_requests(self):
        for i in range(1, 7):  #在页面中找不到最后一页，只能用现成的数字。
        # for i in range(1, 2):  # test
            page_url = self.head_url + 'p' + str(i) + '/'  # 为什么新房的网站就必须加上/？？为什么？？
            yield Request(page_url)

    def parse(self, response):

        divs = response.xpath("//*[@id='container']/div[2]/div[1]/div[4]/div[@class= 'item-mod']")
        for div in divs:
            info_url = div.xpath('@data-link').extract()[0]
            yield Request(info_url, callback=self.get_around_aver)
        """
        div = response.xpath('//*[@id="container"]/div[2]/div[1]/div[4]/div[1]')  #test
        info_url = div.xpath('@data-link').extract()[0]
        yield Request(info_url, callback=self.get_around_aver)
        """
    def get_around_aver(self, response):
        """
        这个函数基本上没有问题。基本上可以保证存在周围价格是能够获取到。并且转化为浮点数。
        :param response:
        :return:
        """
        print(response.url)
        try:  # around_aver有些页面没有这个信息，可能会导致异常。
            around_aver = response.xpath('//*[@id="container"]/div[1]/div[2]/div[1]/dl/dd[2]/span/text()').extract()[0]  # 多了这个span保证如果存在周围价格，则一定能够获取到。
            around_aver = float(around_aver)  # 转化为浮点数
        except:  # 这种方法是没有问题的。可以正确获取到值
            around_aver = 0

        num = re.findall(r'\d+', response.url)[0]
        canshu_url = response.url.replace(num, 'canshu-'+num)
        # print(canshu_url)
        # print(type(around_aver))
        # print(around_aver)
        yield Request(canshu_url, callback=self.get_info, meta={'around_aver': around_aver})

    def get_info(self, response):
        """
        1.每个li都有两个子标签的div,其中div[1]是独立的，div[2]下面还有很多的子标签。
        那么将第一个标签用于判断，第二个标签根据第一个标签来获取值。
        2.使用xpath('string(.)')可以一次获得当前标签以及子标签的所有text
        但是xpath('string(.)')必须要独立使用，不能写成xpath('div/string(.)')的形式。
        3.这里可以用if else语句进行选择
        4.2017年3月24日11:42:26 貌似是写完了，但是没有调试。 还有局部变量要搞清楚
        5.感觉scrapy框架有些不稳定，有时候可以获取到值，有时候不行。为什么？？
        6.还需要进行一些正则表达式的处理。 aver需要获取一个float类型的平均值  两个时间需要获取时间格式的数据  户数需要获得int型的数据。
        7. float型数据：aver,around_aver,use_num
        :param response:
        :return: item
        """
        # 先定义好一些空值，若是没有从网页中获得对应的值则直接返回空值。有一个问题，数字类型获得空字符串会怎么样？？？
        name = "没有数据"
        aver = 0
        around_aver = response.meta['around_aver']
        house_type = "没有数据"
        use = "没有数据"
        developer = "没有数据"
        subdistrict = "没有数据"
        address = "没有数据"
        status = "没有数据"
        start_time = "没有数据"
        give_time = "没有数据"
        use_num = 0
        company = "没有数据"
        build_type = "没有数据"
        source = "安居客"
        link = response.url

        # 要用到的正则表达式
        re_num = re.compile(r"\d+\.?\d*")

        item = NewHouseItem()

        # 获取基本信息中的内容
        base_lis = response.xpath('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul/li')
        for li in base_lis:  # for循环 if else语句不影响变量的作用域，如果变量是灰色则是只对他进行赋值，没有使用。
            # python中没有switch语句。这里暂时用if elif else代替
            div2 = li.xpath('div[2]')
            if li.xpath('div[1]/text()').extract()[0] == '楼盘名称':  # 根据第一个标签的值进行判断选择
                name = div2.xpath('a/text()').extract()[0]
                status = div2.xpath('i/text()').extract()[0]
            # 验证参考单价是否正确————————————————————————————————————————————————————————————————————
            elif li.xpath('div[1]/text()').extract()[0] == '参考单价':  # 1.需要strip()函数 2.得到的使一个字符串 3.有时候得到的不是一个精确地数字而是一个范围 4.可能没有数字，也就是没有span这个标签
                aver = div2.xpath('span/text()').extract()
                if aver:  # 一段含有1or2个数字的字符串，而且前后有空白符。
                    aver = re.findall(re_num, aver[0].strip())
                    aver = sum(map(float, aver)) / len(aver)
                else:
                    aver = 0
            elif li.xpath('div[1]/text()').extract()[0] == '物业类型':  # 其实就是房屋用途
                use = div2.xpath('text()').extract()[0]  # 1.这里是直接获得一个字符串 2.但是可能有多个值 eg.住宅，商住
            elif li.xpath('div[1]/text()').extract()[0] == '开发商':
                developer = div2.xpath('string(.)').extract()[0].strip()  #大部分开发商都是链接，但是有少部分没有公开.不是链接没有在<a></a>中
            elif li.xpath('div[1]/text()').extract()[0] == '区域位置':
                subdistrict = div2.xpath('a[2]/text()').extract()[0] # 貌似第二个a标签是区域位置
            elif li.xpath('div[1]/text()').extract()[0] == '楼盘地址':
                address = div2.xpath('text()').extract()[0]  # 貌似是直接一条文本信息
            else:
                pass

        # 获取销售信息中的内容
        sale_lis = response.xpath('//*[@id="container"]/div[1]/div[1]/div[2]/div[2]/ul/li')
        for li in sale_lis:
            div2 = li.xpath('div[2]')
            if li.xpath('div[1]/text()').extract()[0] == '楼盘户型':
                house_type = div2.xpath('string(.)').extract()[0]  # 这里有多个户型，并且每个户型都在<a>标签中。
                house_type = ''.join(house_type.split())
            elif li.xpath('div[1]/text()').extract()[0] == '开盘时间':
                start_time = div2.xpath('text()').extract()[0]  # 这里的时间格式是XXXX-XX-XX,但是有时会有多余的文本。eg（预计2017年7月交房小高层）
                start_time = ''.join(start_time.split())
                # start_time = self.get_correct_time(start_time)  # 想在这里直接调整时间的格式，但是不造为什么出错。
            elif li.xpath('div[1]/text()').extract()[0] == '交房时间':
                give_time = div2.xpath('text()').extract()[0]  # 这里的时间格式是XXXX-XX-XX,但是1.有时会有多余的文本。eg（预计2017年7月交房小高层）2.甚至有些时候只有一个年份 3.显示数据尚未公开
                give_time = ''.join(give_time.split())
                # give_time = self.get_correct_time(give_time)
            else:
                pass

        # 获取小区信息的内容
        community_lis = response.xpath('//*[@id="container"]/div[1]/div[1]/div[3]/div[2]/ul/li')
        for li in community_lis:
            div2 = li.xpath('div[2]')
            if li.xpath('div[1]/text()').extract()[0] == '建筑类型':
                build_type = div2.xpath('text()').extract()[0]  # 这里有多个类型，以','隔开。是中文的都好还是英文的逗号？
                build_type = ''.join(build_type.split())
            # 验证用户户数是否正确————————————————————————————————————————————————————————————————————————————————————
            elif li.xpath('div[1]/text()').extract()[0] == '规划户数':
                use_num = div2.xpath('text()').extract()[0]  # 往往是户数。当然不仅仅是总户数户数，还有当前户数 eg7800户 （总户数7800户 当期户数4249户）
                use_num = ''.join(use_num.split())
                use_num = re.findall(re_num, use_num)
                use_num = int(use_num[0])  # 这里也许回报索引错误
            elif li.xpath('div[1]/text()').extract()[0] == '物业公司':
                company = div2.xpath('string(.)').extract()[0]  # 1.大部分在<a>标签中，少部分在<div>标签中。 2.这里可以使用string(.)
                company = ''.join(company.split())
            else:
                pass
        '''
        print('name', name)
        print('aver', aver)
        print('around_aver', around_aver)
        print('use', use)
        print('developer', developer)
        print('subdistrict', subdistrict)
        print('address', address)
        print('house_type', house_type)
        print('status', status)
        print('start_time', start_time)
        print('give_time', give_time)
        print('use_num', use_num)
        print('company', company)
        print('build_type', build_type)
        print('source', source)
        print('link', link)
        '''
        item['name'] = name
        item['aver'] = aver
        item['around_aver'] = around_aver
        item['house_type'] = house_type
        item['use'] = use
        item['developer'] = developer
        item['subdistrict'] = subdistrict
        item['address'] = address
        item['status'] = status
        item['start_time'] = start_time
        item['give_time'] = give_time
        item['use_num'] = use_num
        item['company'] = company
        item['build_type'] = build_type
        item['source'] = source
        item['link'] = link
        yield item
