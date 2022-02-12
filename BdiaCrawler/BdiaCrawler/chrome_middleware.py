from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from scrapy.http import HtmlResponse
import time

class chromeMiddleware(object):
    def process_request(self, request, spider):

        if spider.name == "BdiaSpider":
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--ignore-certificate-errors') 
            chrome_options.add_argument('--ignore-ssl-errors') 
            driver = webdriver.Chrome("D:/code/HanedaScra/BdiaCrawler/BdiaCrawler/chromedriver.exe",chrome_options=chrome_options)
            print("Request URL:"+request.url)
            driver.get(request.url)
            time.sleep(3)

            driver.find_element_by_xpath('//div[@class="btn"]').click() # 清除弹窗
            # while(len(driver.find_elements_by_xpath('//div[@class="selectmore"]/span'))):
            while(len(driver.find_elements_by_xpath('//div[@class="selectmore"]/span'))):
                driver.find_element_by_xpath('//div[@class="selectmore"]/span').click()
                time.sleep(1)
            
            print ("Now visiting:"+request.url)
            return HtmlResponse(driver.current_url, body=driver.page_source, encoding='utf-8', request=request)

        else:
            return None