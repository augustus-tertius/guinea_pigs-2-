import scrapy


class TourismCommentItem(scrapy.Item):
    author = scrapy.Field()
    date = scrapy.Field()
    text = scrapy.Field()

