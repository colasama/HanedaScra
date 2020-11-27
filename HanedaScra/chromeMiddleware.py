from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from scrapy.http import HtmlResponse
import time

class chromeMiddleware(object):
    def process_request(self, request, spider):

        if spider.name == "Haneda":
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--ignore-certificate-errors') 
            chrome_options.add_argument('--ignore-ssl-errors') 
            driver = webdriver.Chrome("D:/code/HanedaScra/HanedaScra/chromedriver.exe",chrome_options=chrome_options)

            print("Request URL:"+request.url)
            driver.get(request.url)
            # driver.get("https://tokyo-haneda.com/flight/flightInfo_int.html")

            body = driver.page_source
            print ("访问"+request.url)
            return HtmlResponse(driver.current_url, body=body, encoding='utf-8', request=request)

        else:
            return None