import scrapy
import datetime
from HanedaScra.items import HanedascraItem

class HanedaSpider(scrapy.Spider):
    name = 'Haneda'
    allowed_domains = ['tokyo-haneda.com']
    start_urls = ['https://tokyo-haneda.com/flight/flightInfo_int.html']

    def parse(self, response):
        filename = str(datetime.datetime.now())[0:10]
        items = []

        for each in response.xpath("//*[@id='flightSearch']/div[2]/div[3]/div/div[2]/div[2]/table/tbody"):
            item = HanedascraItem()

            arrivetime = each.xpath("./tr[1]/td[1]/span/text()").extract()
            destination = each.xpath("./tr[1]/td[2]/text()").extract()
            passbyplace = each.xpath("./tr[1]/td[3]/text()").extract()
            # /html/body/div/main/div/div[2]/div[1]/div[2]/div[3]/div/div[2]/div[2]/table/tbody[18]/tr[2]/td[1]/div/a
            # /html/body/div/main/div/div[2]/div[1]/div[2]/div[3]/div/div[2]/div[2]/table/tbody[18]/tr[1]/td[4]/div/a/strong
            
            airline = []
            airline.append(each.xpath("./tr[1]/td[4]/div/a/strong/text()").extract())
            
            if(each.xpath("./tr[1]/td[4]/div/a/strong/text()").extract() == []):
                airline.append(each.xpath("./tr[1]/td[4]/div/span[2]/strong/text()").extract())
                
            for i in range(2,5):
                if(each.xpath("./tr["+str(i)+"]/td[1]/div/a/text()").extract()!=[]):
                    airline.append(each.xpath("./tr["+str(i)+"]/td[1]/div/a/text()").extract())

            flightnumber = each.xpath("./tr[1]/td[5]/text()").extract()
            flightType = each.xpath("./tr[1]/td[6]/text()").extract()
            terminal = each.xpath("./tr[1]/td[7]/span/a/text()").extract()
            checkin = each.xpath("./tr[1]/td[8]/span/a/text()").extract()
            boardinggate = each.xpath("./tr[1]/td[9]/span/a/text()").extract()
            flightstatus = each.xpath("./tr[1]/td[10]/text()").extract()

            if(arrivetime != []):
                item['arrivetime'] = arrivetime[0]
                item['changedtime'] = arrivetime[1]
            if(destination != []):
                item['destination'] = destination[0]
            if(passbyplace != []):
                item['passbyplace'] = passbyplace[0]
            if(airline != []):
                item['airline'] = airline[0]
            if(flightnumber != []):
                item['flightnumber'] = flightnumber[0]
            if(flightType != []):
                item['flightType'] = flightType[0]
            if(terminal != []):
                item['terminal'] = terminal[0]
            if(checkin != []):
                item['checkin'] = checkin[0]
            if(boardinggate != []):
                item['boardinggate'] = boardinggate[0]
            if(flightstatus != []):
                item['flightstatus'] = flightstatus[0]

            items.append(item)

        return items
