from scrapy import Spider
from scrapy.selector import Selector
from lp.items import LpProfile
from lp import settings
import csv


class ProfilesSpider(Spider):
    name = "profiles"
    allowed_domains = ["MAIN_URL_HERE"]
    # start_urls = ['http://pview.findlaw.com/view/4358064_1',
    #               'http://pview.findlaw.com/view/3020130_1',
    #               'http://pview.findlaw.com/view/1724275_1']

    start_urls = []
    with open(settings.lawyer_profile_links_file, 'r') as csvfile:
      data = csv.reader(csvfile)
      for row in data:
        for column in row:
          start_urls.append(column)

    def parse(self, response):
        lawyer_profile = Selector(response).xpath('//div[@class="region"]')

        for profile in lawyer_profile:
            item = LpProfile()

            item['profile_url'] = response.url
            
            try:
              item['name'] = profile.xpath(
                  'div[@id="pp_card"]/div/h1/text()').extract()[0]
            except:
              item['name'] = ""

            try:  
              item['firm'] = profile.xpath(
                  'div[@id="pp_card"]/div/div/a/span[@itemprop="name"]/text()').extract()[0]
            except:
              item['firm'] = ""

            try:  
              item['firm_address_1'] = profile.xpath(
                  'div[@id="pp_card"]/div/div/div/div/div/span[@class="pp_card_street"][1]/text()').extract()[0]
            except:
              item['firm_address_1'] = ""

            try:  
              item['firm_address_2'] = profile.xpath(
                  'div[@id="pp_card"]/div/div/div/div/div/span[@class="pp_card_street"][2]/text()').extract()[0]
            except:
              item['firm_address_2'] = ""

            try:  
              item['firm_city'] = profile.xpath(
                  'div[@id="pp_card"]/div/div/div/div/div/span[@class="pp_card_city"]/text()').extract()[0]
            except:
              item['firm_city'] = ""

            try:  
              item['firm_state'] = profile.xpath(
                  'div[@id="pp_card"]/div/div/div/div/div/span[@class="pp_card_state"]/text()').extract()[0]
            except:
              item['firm_state'] = ""

            try:  
              item['firm_zipcode'] = profile.xpath(
                  'div[@id="pp_card"]/div/div/div/div/div/span[@class="pp_card_zip"]/text()').extract()[0]
            except:
              item['firm_zipcode'] = ""

            try:
              item['firm_phone_1'] = profile.xpath(
                  'div[@id="pp_card"]/div/div/div/div/div[@class="pp_card_phone"]/div/span[@itemprop="telephone"][1]/text()').extract()[0]
            except:
              item['firm_phone_1'] = ""

            try:  
              item['firm_phone_2'] = profile.xpath(
                  'div[@id="pp_card"]/div/div/div/div/div[@class="pp_card_phone"]/div/span[@itemprop="telephone"][2]/text()').extract()[0]
            except:
              item['firm_phone_2'] = ""

            try:  
              item['firm_fax'] = profile.xpath(
                  'div[@id="pp_card"]/div/div/div/div/div[@class="pp_card_phone"]/div/span[@itemprop="faxNumber"]/text()').extract()[0]
            except:
              item['firm_fax'] = ""

            try:
              item['firm_url'] = profile.xpath(
                  'div[@id="pp_card"]/div/div/div/div/div[@class="pp_card_url"][1]/a/@href').extract()[0]
            except:
              item['firm_url'] = ""

            try:
              item['position'] = profile.xpath(
                  'div[@id="pp_overview"]/div[2]/div/span[@class="block_content_item"]/text()').extract()[0]
            except:
              item['position'] = ""

            try:
              item['practice_area_1'] = profile.xpath(
                'div[@id="pp_overview"]/div[4]/div/span[@class="block_content_item"][1]/text()').extract()[0]
            except:
              item['practice_area_1'] = ""

            try:
              item['practice_area_2'] = profile.xpath(
                'div[@id="pp_overview"]/div[4]/div/span[@class="block_content_item"][2]/text()').extract()[0]
            except:
              item['practice_area_2'] = ""

            try:
              item['practice_area_3'] = profile.xpath(
                'div[@id="pp_overview"]/div[4]/div/span[@class="block_content_item"][3]/text()').extract()[0]
            except:
              item['practice_area_3'] = ""

            try:
              item['practice_area_4'] = profile.xpath(
                'div[@id="pp_overview"]/div[4]/div/span[@class="block_content_item"][4]/text()').extract()[0]
            except:
              item['practice_area_4'] = ""

            try:
              item['practice_area_5'] = profile.xpath(
                'div[@id="pp_overview"]/div[4]/div/span[@class="block_content_item"][5]/text()').extract()[0]
            except:
              item['practice_area_5'] = ""

            try:
              item['practice_area_6'] = profile.xpath(
                'div[@id="pp_overview"]/div[4]/div/span[@class="block_content_item"][6]/text()').extract()[0]
            except:
              item['practice_area_6'] = ""

            yield item