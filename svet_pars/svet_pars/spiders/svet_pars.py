import scrapy


class SvetParsSpider(scrapy.Spider):
    name = "svet_pars"
    allowed_domains = ["https://www.divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        pass
