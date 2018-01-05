# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TaobaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    class1 = scrapy.Field()
    class2 = scrapy.Field()
    
class TaobaoDataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    sales = scrapy.Field()
    store = scrapy.Field()
    class1 = scrapy.Field()
    class2 = scrapy.Field()
    


