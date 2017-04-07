# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CookItem(scrapy.Item):
    name = scrapy.Field()
    prep_time = scrapy.Field()
    cook_time = scrapy.Field()
    description = scrapy.Field()
    ingredients = scrapy.Field()
    method = scrapy.Field()
    tags = scrapy.Field()
    category = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()