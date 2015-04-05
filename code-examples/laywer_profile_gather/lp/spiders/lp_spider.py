from scrapy import Spider
from scrapy.selector import Selector
from lp.items import LpItem
from lp import settings
import csv


class LpSpider(Spider):
    name = "lp"
    allowed_domains = ["MAIN_URL_HERE"]
    start_urls = []

    with open(settings.start_urls_file, 'r') as csvfile:
      data = csv.reader(csvfile)
      for row in data:
        for column in row:
          start_urls.append(column)

    def parse(self, response):
        lawyers = Selector(response).xpath('//div[@class="block_content"]/a')

        for lawyer in lawyers:
            item = LpItem()
            item['profile_link'] = lawyer.xpath(
                '@href').extract()[0]
            item['name'] = lawyer.xpath(
                'div[@class="bp_listings_result_header"]/text()').extract()[0]
            item['address_locality'] = lawyer.xpath(
                'div[@class="bp_listings_result_address"]/span[@itemprop="addressLocality"]/text()').extract()[0]
            item['address_region'] = lawyer.xpath(
                'div[@class="bp_listings_result_address"]/span[@itemprop="addressRegion"]/text()').extract()[0]
            item['job_title'] = lawyer.xpath(
                'div[@class="bp_listings_result_description"]/text()').extract()[0]
            yield item
