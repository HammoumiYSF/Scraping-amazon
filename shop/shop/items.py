# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ShopItem(scrapy.Item):
    product_name = scrapy.Field(default=u'')
    product_price = scrapy.Field(default=u'')
    product_image = scrapy.Field(default=u'')
    
