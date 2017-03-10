from .sql_lianjia2 import SQLLianjia2
from SpyderofHuangdaoHouse.items import Lianjia2Item
import logging


class Lianjia2Pipeline(object):

    logger = logging.getLogger()

    def process_item(self, item, spider):

        self.logger.info('come into pipeline!!!!!!!!!!!!!!!!!!')
        if isinstance(item, Lianjia2Item):
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
            self.logger.info('start to execute sql........................')
            SQLLianjia2.insert_data(name, price, aver, build_time, subdistrict, community, source, link, area, house_type, floor, decoration, orientation, build_type, structure, use)