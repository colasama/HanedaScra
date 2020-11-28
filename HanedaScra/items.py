# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class HanedascraItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    arrivetime = scrapy.Field()         # 整点到达时间
    changedtime = scrapy.Field()        # 改签时间
    destination = scrapy.Field()        # 目的地
    passbyplace = scrapy.Field()        # 经由地
    airline = scrapy.Field()            # 航班名称
    flightnumber = scrapy.Field()       # 航班号
    flightType = scrapy.Field()         # 飞机型号
    terminal = scrapy.Field()           # 候机楼
    checkin = scrapy.Field()            # 值班柜台
    boardinggate = scrapy.Field()       # 登机口
    flightstatus = scrapy.Field()       # 现在的情况
    
    pass
