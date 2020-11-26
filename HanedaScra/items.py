# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HanedascraItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    startTime = scrapy.Field()
    startPlace = scrapy.Field()
    passPlace = scrapy.Field()
    flightCom = scrapy.Field()
    flightNo = scrapy.Field()
    flightType = scrapy.Field()
    arriveStation = scrapy.Field()
    checkIn = scrapy.Field()
    boardGate = scrapy.Field()
    flightStatus = scrapy.Field()
    
    pass
