import scrapy


class SvetnewparsSpider(scrapy.Spider):
    name = "svetnewpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://divan.ru"]

    def parse(self, response):
        pass
