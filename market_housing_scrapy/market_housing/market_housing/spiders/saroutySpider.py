import scrapy


class SaroutyspiderSpider(scrapy.Spider):
    name = "saroutySpider"
    allowed_domains = ["sarouty.ma"]
    start_urls = ["https://www.sarouty.ma/fr/recherche?c=1&fu=0&ob=mr&page=1"]

    def parse(self, response):
        pass
