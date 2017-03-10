# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Lianjia2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    aver = scrapy.Field()
    build_time = scrapy.Field()
    area = scrapy.Field()
    house_type = scrapy.Field()
    floor = scrapy.Field()
    subdistrict = scrapy.Field()
    community = scrapy.Field()
    # address = scrapy.Field()  #not find accurate address
    source = scrapy.Field()
    link = scrapy.Field()
    decoration = scrapy.Field()
    orientation = scrapy.Field()
    build_type = scrapy.Field()
    structure = scrapy.Field()
    use = scrapy.Field()
