import scrapy


class QiitaTrendSpider(scrapy.Spider):
    name = "qiita_trend"
    allowed_domains = ["qiita.com"]
    start_urls = ["https://qiita.com"]

    def parse(self, response):
        category = response.xpath('//div[@class="style-ghw6r8"]/a[@href="/"]/text()').get()
        titles = response.xpath('//h2/a/text()').getall()
        urls = response.xpath('//h2/a/@href').getall()

        yield {
            'category':category,
            'titles':titles,
            'urls':urls,
        }