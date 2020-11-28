import requests
import json
import urllib3
import datetime
import uagent
import re

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
        print("被远程主机关闭连接了！可能是被识别到是爬虫了？")
        return None

def jsonParse(json):
    # print(str(json['flight_info'][0]))
    items = []
    pattern= str(datetime.datetime.now())[0:10].replace('-','/')

    for jsonpart in json['flight_info']:
        item = {}
        # print(jsonpart)
        if(re.search(pattern, jsonpart['定刻'])==None):
            continue

        item['arrivetime'] = jsonpart['定刻']          # 整点到达时间
        item['changedtime']  = jsonpart['変更時刻']         # 改签时间
        item['destination'] = jsonpart['行先地空港和名称']        # 目的地
        item['passbyplace'] = jsonpart['経由地空港和名称']         # 经由地
        item['airline'] = []
        item['flightNo'] = []
        for each in jsonpart['航空会社']:
            item['airline'].append(each['ＡＬ和名称'])
            item['flightNo'].append(each['便名'])
        item['flighttype'] = jsonpart['機種コード']         # 飞机型号
        item['terminal'] = jsonpart["ターミナル区分"]           # 候机楼
        item['checkin'] = jsonpart['チェックインカウンター番号']            # 值班柜台
        item['flightstatus'] = jsonpart['備考訳名称']['ja']           # 现在的情况

        items.append(item)
    return items

if __name__ == "__main__":
    filename = str(datetime.datetime.now())[0:10]
    content = getJson()
    if (content == None):
        exit(0)
    jsonFile = json.loads(content)
    resultDict = jsonParse(jsonFile)
    
    with open(filename+".json", 'w',encoding="utf8") as f:
        json.dump(resultDict,f,ensure_ascii=False,indent=4)
    print(filename+ " 数据爬取成功！")
    pass
