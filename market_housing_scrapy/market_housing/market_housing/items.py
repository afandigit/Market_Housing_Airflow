import scrapy
from itemloaders.processors import MapCompose, TakeFirst, Join
from w3lib.html import remove_tags

def remove_useless_charcaters(value):
    return " ".join(str(value).replace("\t", " ").replace("\n", " ").split())

class MubawabItem(scrapy.Item):

    advertisement_url       = scrapy.Field(output_processor = TakeFirst())
    advertisement_type       = scrapy.Field(output_processor = TakeFirst())
    title                   = scrapy.Field(input_processor = MapCompose(remove_useless_charcaters, remove_tags) , output_processor = TakeFirst())
    price                   = scrapy.Field(input_processor = MapCompose(remove_useless_charcaters, remove_tags) , output_processor = TakeFirst())
    publication_date        = scrapy.Field(input_processor = MapCompose(remove_useless_charcaters, remove_tags) , output_processor = TakeFirst())
    location                = scrapy.Field(input_processor = MapCompose(remove_useless_charcaters, remove_tags) , output_processor = TakeFirst())
    description             = scrapy.Field(input_processor = MapCompose(remove_useless_charcaters, remove_tags) , output_processor = Join(separator=';'))
    complete_description    = scrapy.Field(input_processor = MapCompose(remove_useless_charcaters, remove_tags) , output_processor = TakeFirst())
    features_list           = scrapy.Field(input_processor = MapCompose(remove_useless_charcaters, remove_tags) , output_processor = Join(separator=';'))
    website_name            = scrapy.Field(output_processor = TakeFirst())



class AvitoItem(scrapy.Item):

    advertisement_url       = scrapy.Field(output_processor = TakeFirst())
    advertisement_type       = scrapy.Field(output_processor = TakeFirst())
    title                   = scrapy.Field(input_processor = MapCompose(remove_useless_charcaters, remove_tags) , output_processor = TakeFirst())
    price                   = scrapy.Field(input_processor = MapCompose(remove_useless_charcaters, remove_tags) , output_processor = TakeFirst())
    publication_date        = scrapy.Field(input_processor = MapCompose(remove_useless_charcaters, remove_tags) , output_processor = TakeFirst())
    location                = scrapy.Field(input_processor = MapCompose(remove_useless_charcaters, remove_tags) , output_processor = TakeFirst())
    description             = scrapy.Field(input_processor = MapCompose(remove_useless_charcaters, remove_tags) , output_processor = Join(separator=';'))
    complete_description    = scrapy.Field(input_processor = MapCompose(remove_useless_charcaters, remove_tags) , output_processor = TakeFirst())
    features_list           = scrapy.Field(input_processor = MapCompose(remove_useless_charcaters, remove_tags) , output_processor = Join(separator=';'))
    website_name            = scrapy.Field(output_processor = TakeFirst())
