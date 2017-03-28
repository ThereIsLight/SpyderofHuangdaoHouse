from SpyderofHuangdaoHouse.items import NewHouseItem
from .sql_anjuke import AnjukeSQL
import logging
import re


class AnjukePipeline(object):

    logger = logging.getLogger()

    def get_correct_time(self, str):
        """
        将开盘时间与交房时间转化为指定的格式。
        总结提取到的开盘时间与交房时间的格式
        1.尚未公开(没有任何数字)
        2.明确的年月日 格式为XXXX-XX-XX。
        3.只有年份 格式为XXXX
        4.有明确的年月日，但是还包含其他的信息。例如2017-05-31  （预计2017年5月交付）
        5.只有年份月份，没有日期。XXXX-XX
        """
        res = re.findall(r"\d{4}-\d{1,2}-\d{1,2}", str)
        if not res:
            res = re.findall(r"\d{4}-\d{1,2}", str)
            if not res:
                res = re.findall(r"\d{4}", str)
                if not res:
                    return str  # 直接返回尚无数据
                else:
                    return res[0] + '-12' + '-30'  # 直接返回年+月份12+日期30
            else:
                return res[0] + "-01"  # 直接返回年月+日期为01
        else:
            return res[0]  # 直接返回年月日

    def process_item(self, item, spider):

        self.logger.info('come into anjuke pipeline!!!!!!!!!!!!!!!!!!')
        if isinstance(item, NewHouseItem):
            name = item['name']
            aver = item['aver']
            around_aver = item['around_aver']
            house_type = item['house_type']
            use = item['use']
            developer = item['developer']
            subdistrict = item['subdistrict']
            address = item['address']
            source = item['source']
            link = item['link']
            status = item['status']
            start_time = self.get_correct_time(item['start_time'])
            give_time = self.get_correct_time(item['give_time'])
            use_num = item['use_num']
            company = item['company']
            build_type = item['build_type']
            self.logger.info('start to execute sql........................')
            AnjukeSQL.insert_data(name, aver, around_aver, house_type, use, developer, subdistrict, address, status,
                                  start_time, give_time, use_num, company, build_type , source, link)

