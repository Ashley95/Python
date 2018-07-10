# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MafengwoItem(scrapy.Item):
    collections = 'Mafengwo'
    # define the fields for your item here like:
    area = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    href = scrapy.Field()


