# -*- coding: utf-8 -*-
# DATA.GOV.HK Datasets Scraper
# Sammy Fung <sammy@sammy.hk>
import scrapy
from data_gov_hk.items import DataGovHkItem

class DataGovhkSpider(scrapy.Spider):
  name = "data_govhk"
  allowed_domains = ["data.gov.hk"]
  start_urls = (
    'http://www.data.gov.hk/',
  )

  def parse(self, response):
    for i in response.xpath("//h3/a[contains(@class, 'media-view')]/@href").extract():
      yield scrapy.Request("http://www.data.gov.hk%s"%i, callback=self.parse_category)

  def parse_category(self, response):
    for i in response.xpath("//h3[contains(@class, 'dataset-heading')]/a/@href").extract():
      yield scrapy.Request("http://www.data.gov.hk%s"%i, callback=self.parse_dataset)

  def parse_dataset(self, response):
    title = response.xpath("//h3[contains(@id, 'resourceModalLabel')]/text()").extract()[0]
    provider = response.xpath("//img[contains(@class, 'media-image')]/@alt").extract()
    category = response.xpath("//a[contains(@class, 'badge')]/text()").extract()
    updateFreq = response.xpath("//section[contains(@class, 'additional-info')]/table/tbody/tr/td/text()").extract()[1]
    scrapedTime = response.headers['Date']
    resource_name = response.xpath("//div[contains(@class, 'dataset-resource-name')]/div/div/a/@title").extract()
    resource_format = response.xpath("//div[contains(@class, 'dataset-resource-format')]/span/text()").extract() 
    resource_download = response.xpath("//div[contains(@class, 'dataset-resource-download')]/a/@href").extract()
    for i in range(0, len(resource_name)):
      item = DataGovHkItem()
      item['datasetTitle'] = title
      item['resourceName'] = resource_name[i]
      item['resourceFormat'] = resource_format[i]
      item['resourceURL'] = resource_download[i]
      item['sourceUrl'] = response.url
      item['provider'] = provider
      item['category'] = category
      item['updateFreq'] = updateFreq
      item['scrapedTime'] = scrapedTime
      yield item

