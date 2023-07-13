import scrapy


class QiitaTrendSpider(scrapy.Spider):
    name = "qiita_trend"
    allowed_domains = ["qiita.com"]
    start_urls = ["https://qiita.com"]

    def parse(self, response):
        pass
