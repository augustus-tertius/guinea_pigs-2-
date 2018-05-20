from scrapy.crawler import CrawlerProcess

import tourism.settings as crawler_settings
import tourism.spiders as spiders


def load_comments():
    process = CrawlerProcess(vars(crawler_settings))
    process.crawl(spiders.TourismSpider)
    process.start()  # the script will block here until the crawling is finished