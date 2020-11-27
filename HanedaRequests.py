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
    html = requests.get(url,headers=headers,verify=False)
    html = html.content
    return html

def jsonParse(json):
    print(str(json['flight_info'][0]))
    return

if __name__ == "__main__":
    dateTime = str(datetime.datetime.now())[0:10]
    content = getJson()
    jsonFile = json.loads(content)

    jsonParse(jsonFile)
    
    pass
    # pass