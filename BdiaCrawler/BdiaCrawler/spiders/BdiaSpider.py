import scrapy
import datetime
from BdiaCrawler.items import BdiacrawlerItem

class BdiaSpider(scrapy.Spider):
    name = 'BdiaSpider'
    allowed_domains = ['bdia.com.cn']
    start_urls = ['https://www.bdia.com.cn/#/flightdep']

    def parse(self, response):
        filename = str(datetime.datetime.now())[0:10]
        items = []

        i = 0
        for each in response.xpath('//div[@class="flight-block owh"]'):
            i = i + 1
            print(each)
            # if(i == 1):
            #     print("Pass First Div.")
            #     continue
            item = BdiacrawlerItem()
            plan_departure_time = each.xpath('.//span[@class="plan-time flight-t"]/text()').extract()
            acture_departure_time = each.xpath('.//span[@class="actual-time flight-t"]/text()').extract()
            est_departure_time = each.xpath('.//span[@class="estimate-time flight-t"]/text()').extract()
            flight_company = each.xpath('.//div[@class="company-name"]/span/span/text()').extract()
            flight_number = each.xpath('.//div[@class="airline-code"]/span/text()').extract()
            flight_destination = each.xpath('.//div[@class="destination-place"]/span/text()').extract()
            flight_check_in =each.xpath('.//div[@class="checkin-box"]/span/text()').extract()
            boarding_port = each.xpath('.//div[@class="boarding-box"]/span/text()').extract()
            flight_stat = each.xpath('.//div[@class="takeoff-state block-li"]/span/text()').extract()

            item['plan_departure_time'] = plan_departure_time[0]
            if(acture_departure_time != []):
                item['acture_departure_time'] = acture_departure_time[0]
            else:
                item['acture_departure_time'] = None
            if(est_departure_time != []):
                item['est_departure_time'] = est_departure_time[0].replace("预计\n                            ","")
            else:
                item['est_departure_time'] = None
            item['flight_company'] = flight_company
            item['flight_number'] = flight_number
            item['flight_destination'] = flight_destination[0]
            item['flight_check_in'] = flight_check_in[0]
            if(boarding_port != []):
                item['boarding_port'] = boarding_port[0]
            else:
                item['boarding_port'] = None
            item['flight_stat'] = flight_stat[0]
            items.append(item)
            
        return items