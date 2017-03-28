from SpyderofHuangdaoHouse.items import ResoldHouseItem
from .sql_lianjia2 import Lianjia2SQL
import logging


class Lianjia2Pipeline(object):

    logger = logging.getLogger()

    def process_item(self, item, spider):
        self.logger.info('come into lianjia2 pipeline!!!!!!!!!!!!!!!!!!')
        if isinstance(item, ResoldHouseItem):
            name = item['name']
            price = item['price']
            aver = item['aver']
            build_time = item['build_time']
            area = item['area']
            house_type = item['house_type']
            floor = item['floor']
            subdistrict = item['subdistrict']
            community = item['community']
            source = item['source']
            link = item['link']
            decoration = item['decoration']
            orientation = item['orientation']
            build_type = item['build_type']
            structure = item['structure']
            use = item['use']
            address = '暂无数据'
            self.logger.info('start to execute sql........................')
            Lianjia2SQL.insert_data(name, price, aver, build_time, subdistrict, community, address, source, link, area, house_type, floor, decoration, orientation, build_type, structure, use)