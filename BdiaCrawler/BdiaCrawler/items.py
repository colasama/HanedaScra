# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BdiacrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    plan_departure_time = scrapy.Field()    # 计划起飞时间
    acture_departure_time = scrapy.Field()  # 实际起飞时间
    est_departure_time = scrapy.Field()     # 预计起飞时间
    flight_company = scrapy.Field()         # 航空公司
    flight_number = scrapy.Field()          # 航班号
    flight_destination = scrapy.Field()     # 目的地
    flight_check_in = scrapy.Field()        # 值机柜台
    boarding_port = scrapy.Field()          # 登机口
    flight_stat = scrapy.Field()            # 状态
    
    pass
