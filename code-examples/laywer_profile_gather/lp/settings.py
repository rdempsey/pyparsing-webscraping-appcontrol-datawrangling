# -*- coding: utf-8 -*-

# Scrapy settings for lp project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'lp'

SPIDER_MODULES = ['lp.spiders']
NEWSPIDER_MODULE = 'lp.spiders'

# Be nice to the sites we're crawling
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5.0
AUTOTHROTTLE_MAX_DELAY = 60.0
DOWNLOAD_DELAY = 5

# Disable cookies
COOKIES_ENABLED = False

# Define which pipeline we'll use
ITEM_PIPELINES = ['lp.pipelines.ProfilesPipeline']

# On the Pi
start_urls_file = '/home/pi/Dev/profile_gather/lp/data/start_urls.csv'
lawyer_profile_links_file = '/home/pi/Dev/profile_gather/lp/data/lawyer_profile_urls_updated.csv'
lawyer_profiles_file = '/home/pi/Dev/profile_gather/lp/data/lawyer_profiles.csv'

# Use the fake_useragent python library
# Requires you to: pip install fake-useragent
DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
    'lp.middlewares.RandomUserAgentMiddleware': 400,
}