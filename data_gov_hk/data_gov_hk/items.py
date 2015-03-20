# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DataGovHkItem(scrapy.Item):
  datasetTitle = scrapy.Field()
  resourceName = scrapy.Field()
  resourceFormat = scrapy.Field()
  resourceURL = scrapy.Field()
  sourceUrl = scrapy.Field()
  provider = scrapy.Field()
  category = scrapy.Field()
  updateFreq = scrapy.Field()
  scrapedTime = scrapy.Field()
