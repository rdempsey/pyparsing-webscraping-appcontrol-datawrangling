# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LpItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    address_locality = scrapy.Field()
    address_region = scrapy.Field()
    job_title = scrapy.Field()
    profile_link = scrapy.Field()
    pass

class LpProfile(scrapy.Item):
    profile_url = scrapy.Field()
    name = scrapy.Field()
    firm = scrapy.Field()
    firm_address_1 = scrapy.Field()
    firm_address_2 = scrapy.Field()
    firm_city = scrapy.Field()
    firm_state = scrapy.Field()
    firm_zipcode = scrapy.Field()
    firm_phone_1 = scrapy.Field()
    firm_phone_2 = scrapy.Field()
    firm_fax = scrapy.Field()
    firm_url = scrapy.Field()
    position = scrapy.Field()
    practice_area_1 = scrapy.Field()
    practice_area_2 = scrapy.Field()
    practice_area_3 = scrapy.Field()
    practice_area_4 = scrapy.Field()
    practice_area_5 = scrapy.Field()
    practice_area_6 = scrapy.Field()
    pass
