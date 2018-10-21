# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewscrawlerItem(scrapy.Item):
    headline = scrapy.Field()
    author = scrapy.Field()
    articleUrl = scrapy.Field()
    articleText = scrapy.Field()
