# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log
import csv
import string
import unicodedata
from lp import settings

exclude = set(string.punctuation)


def fully_clean_item(x):
  """
  Helper function to perform all the available cleanings
  """
  # Remove unicode characters
  x = str(x.encode('utf8'))
  # Remove extra commas
  x = x.replace(",","")
  # Remove extra whitespace from the front and back
  x = x.strip()
  # Remove all extra line breaks and tabs
  x = x.replace("\n","")
  x = x.replace("\t","")
  return x


def write_to_csv(item):
  writer = csv.writer(open(settings.lawyer_profile_links_file, 'a'), lineterminator='\n')
  writer.writerow([item[key] for key in item.keys()])


def write_to_profiles_csv(item):
  writer = csv.writer(open(settings.lawyer_profiles_file, 'a'), lineterminator='\n')
  writer.writerow([item[key] for key in item.keys()])
       

class LpPipeline(object):
  def process_item(self, item, spider):
    write_to_csv(item)
    return item


class ProfilesPipeline(object):
  def process_item(self, item, spider):
    for key in item.keys():
      item[key] = fully_clean_item(item[key])
    write_to_profiles_csv(item)
    return item
