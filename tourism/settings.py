
BOT_NAME = 'tourism'

SPIDER_MODULES = ['tourism.spiders']
NEWSPIDER_MODULE = 'tourism.spiders'
ROBOTSTXT_OBEY = True
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36'
CONCURRENT_REQUESTS = 32
DOWNLOAD_DELAY = 0.25
COOKIES_ENABLED = False
ITEM_PIPELINES = {
    'tourism.pipelines.MongoPipeline': 300,
}
LOG_ENABLED=False
MONGO_URI = 'mongodb://localhost:27017'
MONGO_DATABASE = 'comments'
