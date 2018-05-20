# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TourismCommentItem(scrapy.Item):
    author = scrapy.Field()
    date = scrapy.Field()
    text = scrapy.Field()
