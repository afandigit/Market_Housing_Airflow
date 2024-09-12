import scrapy
from housemarketing_scrapy.items import AvitoItem
from scrapy.loader import ItemLoader
from scrapy_selenium import SeleniumRequest



class AvitoSpider(scrapy.Spider):
    name = "avito"
    allowed_domains = ["www.avito.ma"]
    start_urls = ["https://www.avito.ma/fr/maroc/immobilier"]

    def start_requests(self):
        url = 'https://www.avito.ma/fr/maroc/immobilier'
        yield SeleniumRequest(url=url, callback=self.parse, wait_time=3)

    def parse(self, response):

        avito_annoncements_href = response.xpath('//div[@class="sc-1nre5ec-1 crKvIr listing"]/a[@href]/@href').getall()
        if len(avito_annoncements_href)>0:
            for estate_announcement_link in avito_annoncements_href:
                # yield response.follow(estate_announcement_link, callback=self.parse_avito_estate_announcement)
                #  yield SeleniumRequest(url=estate_announcement_link, 
                #                        callback=self.parse_avito_estate_announcement, 
                #                        wait_time=10,
                #                        script='document.querySelector(".sc-ij98yj-1.eVxSeD").click()')
                yield SeleniumRequest(url=estate_announcement_link, 
                                       callback=self.parse_avito_estate_announcement, 
                                       wait_time=10)

        next_page_url = response.xpath("//a[@class='sc-1cf7u6r-0 gRyZxr sc-2y0ggl-1 yRCEb activePage']/following-sibling::a/@href").get()
        if next_page_url:
            yield SeleniumRequest(url=next_page_url, callback=self.parse)

    def parse_avito_estate_announcement(self, response):
        # driver = response.request.meta['driver'] # This line didn't work !!!!!

        l = ItemLoader(item=AvitoItem(), selector=response)

        # button = driver.get_element_by_xpath( '//button[@class="sc-ij98yj-1 eVxSeD"]')
        # button.click()
        
        l.add_value('advertisement_url', response.url)
        l.add_value('advertisement_type', "none")
        l.add_xpath('title', '//div[@class="sc-1g3sn3w-8 ePtCCn"]//h1')
        l.add_xpath('price', '//div[@class="sc-1g3sn3w-8 ePtCCn"]//p')
        l.add_xpath('publication_date', '//div[@class="sc-1g3sn3w-7 bNWHpB"]//time')
        l.add_xpath('location', '//div[@class="sc-1g3sn3w-7 bNWHpB"]//span[1]')
        l.add_value('description', '')
        # print(response.xpath('//div[@class="sc-1g3sn3w-16 fDMtTb"]//p').getall()) --- This line display the 'complete_description' to check if its gonna grap all text or not. using Selenium to add click event on a button.
        # print(response.xpath('//div[@class="sc-1g3sn3w-7 bNWHpB"]//svg[@aria-labelledby="MapPinFillTitleID"]/following-sibling::span').get()) -- check if we can grap 'svg' element using selenuim
        l.add_xpath('complete_description', '//div[@class="sc-1g3sn3w-16 fDMtTb"]//p')
        l.add_xpath('features_list', '//div[@class="sc-qmn92k-0 cjptpz"]//span')
        l.add_value('website_name', 'avito')

        yield l.load_item()
