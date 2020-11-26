import scrapy
from HanedaScra.items import HanedascraItem

class HanedaSpider(scrapy.Spider):
    name = 'Haneda'
    allowed_domains = ['tokyo-haneda.com']
    start_urls = ['http://tokyo-haneda.com/flight/flightInfo_int.html']

    def parse(self, response):
        filename = "flightInfo_int.html"
        items = []
        # print(response.body)
        # pass
        print("===============")
        print("Here is a Test.")
        print("===============")
        print(response.xpath("//table/tbody[1]/tr[1]/td[1]"))

        for each in response.xpath("//table"):
            item = HanedascraItem()
            #targetFile = open("target.html",'w',encoding="utf8")
            #targetFile.write(str(response.body))
            
            name = each.xpath("/tbody[1]/tr[1]/td[1]/span[1]").extract()
            print("Content: "+name)
            # print()
            #open(filename,'w').write(response.body)
        pass

# /html/body/div/main/div/div[2]/div[1]/div[2]/div[3]/div/div[2]/div[2]/table/tbody[1]/tr[1]/td[1]
# //*[@id="flightSearch"]/div[2]/div[3]/div/div[2]/div[2]/table/tbody[1]/tr[1]/td[1]/span[1]
# https://tokyo-haneda.com/app_resource/flight/data/int/hdacfdep.json