import scrapy


class Svet_parsSpider(scrapy.Spider):
    name = "svet_pars"
    allowed_domains = ["www.divan.ru", "divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        svets = response.css('div._Ud0k')
        for svet in svets:
            name = svet.css("div.wYUX2 span::text").get()
            price = svet.css("div.pY3d2 span::text").get()
            url = svet.css("a").attrib.get("href")

            if name and price and url:
                yield {
                    "name": name,
                    "price": price,
                    "url": url
                }