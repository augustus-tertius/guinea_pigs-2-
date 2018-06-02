import scrapy
from tourism import TourismCommentItem


class TourismSpider(scrapy.Spider):
    name = "tourism"
    allowed_domains = ["forum.rukzak.ua"]
    start_urls = ["https://forum.rukzak.ua/viewforum.php?f=10&sid=633c3f063449ab6aa47bc5d3424cb276/viewtopic.php?f=10&t=5875"]

    comment_xpath = '//div[@class="inner"]'

    next_page_xpath = '//div[@class="pagination"]/ul/li[@class="arrow next"]/e/@href'
    item_links_xpath = '//div[@class="inner"]/ul[@class="topiclist topics"]/li/dl/dt/div/e/@href'
    fields = {
        'author': '//p[@class="author"]/span/strong/e[@class="username"]/text()',
        'date': '//p[@class="author"]/child::text()[last()]',
        'text': '//div[@class="postbody"]//div[@class="content"]/child::text()'
    }

    def parse(self, response):
        try:
            next_page = response.xpath(self.next_page_xpath).extract_first()
            if next_page:
                # yield response.follow(response.joinurl(next_page))
                response.follow(response.urljoin(next_page))
        except Exception as e:
            print("ERROR: " + str(e))
        return self.parse_discussions(response)

    def parse_discussions(self, response):
        item_links = [a.extract() for a in response.xpath(self.item_links_xpath)]
        print(len(item_links))
        for item_link in item_links:
            try:
                yield response.follow(response.urljoin(item_link), self.parse_item)
            except Exception as e:
                print(e)

    def parse_item(self, response):
        try:
            comments_list = response.xpath(self.comment_xpath)
            print(len(comments_list))
            for comment in comments_list:
                yield self.parse_comment(comment)
        except Exception as e:
            print("ERROR "+str(e))

    def parse_comment(self, comment):
        try:
            comment_item = TourismCommentItem()
            for name, xpath in self.fields.items():
                v = comment.xpath(xpath).extract_first()
                if v:
                    comment_item[name]=v.strip()
            return comment_item
        except Exception as e:
            print("ERROR: " + str(e))
