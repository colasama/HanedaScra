import requests
import json
import urllib3
import datetime
import uagent

urllib3.disable_warnings()
url = "https://tokyo-haneda.com/app_resource/flight/data/int/hdacfdep.json"

def getJson():
    ua = uagent.randomUserAgent()
    headers = {
        "User-Agent": ua
    }
    try:
        html = requests.get(url,headers=headers,verify=False)
        html = html.content
        return html
    except requests.exceptions.RequestException as e:
        print(e)
        print("奇怪的错误增加了！")
        pass

def jsonParse(json):
    print(str(json['flight_info'][0]))
    
    i = 0
    while(i != -1):
        jsonpart = json['flight_info'][i]
        
        arrivetime = jsonpart[]          # 整点到达时间
        changedtime = jsonpart[]         # 改签时间
        destination = jsonpart[]        # 目的地
        passbyplace = jsonpart[]         # 经由地
        airline = jsonpart[]             # 航班名称
        flightNo = jsonpart[]           # 航班号
        flightType = jsonpart[]         # 飞机型号
        terminal = jsonpart[]           # 候机楼
        checkin = jsonpart[]            # 值班柜台
        boardinggate = jsonpart[]       # 登机口
        flightStatus = jsonpart[]           # 现在的情况
    return

if __name__ == "__main__":
    dateTime = str(datetime.datetime.now())[0:10]
    content = getJson()
    jsonFile = json.loads(content)

    jsonParse(jsonFile)
    
    pass
    # pass

