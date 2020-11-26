import requests
import json
import urllib3
import datetime

urllib3.disable_warnings()
url = "https://tokyo-haneda.com/app_resource/flight/data/int/hdacfdep.json"

def getJson():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
    }
    html = requests.get(url,headers=headers,verify=False)
    html = html.content
    return html

def jsonParse(json):
    pass

if __name__ == "__main__":
    content = getJson()
    jsonFile = json.loads(content)
    # jsonParse(jsonFile)
    
    print(datetime.datetime.now().ctime)
    print(str(jsonFile['flight_info'][0]))
    
    pass