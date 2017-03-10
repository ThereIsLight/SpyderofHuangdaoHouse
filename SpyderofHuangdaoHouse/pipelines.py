# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import logging

# ??????????????????????????????????
# 试了很多遍都没将数据写入文件，但是加了几个logger之后，马上成功了，为什么？？谁能告诉我
class SpyderofhuangdaohousePipeline(object):

    logger = logging.getLogger()

    def __init__(self):
        self.file = open('items.jl', 'w')
        self.logger.info('Now i write a file!!!!!!!!!')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        self.logger.info('now i write data to the file!!!!!!!!!!')
        return item