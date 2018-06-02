from scrapy.crawler import CrawlerProcess

import tourism.settings as crawler_settings
import tourism.spiders as spiders


def load_comments():
    print("here 1")
    process = CrawlerProcess(vars(crawler_settings))
    print("here 2")
    process.crawl(spiders.TourismSpider)
    print("here 3")
    process.start()  # the script will block here until the crawling is finished
