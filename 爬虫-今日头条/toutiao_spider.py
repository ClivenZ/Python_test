import requests
import time
import json
from utils import get_random_browser

def get_resquest_url_and_headers():
    user_agent = get_random_browser()
    current_time = int(time.time())
    headers={
        "user-agent":user_agent
    }
    proxies = {
        "url": "https://125.110.89.147:9000"
    }
    base_url = "https://www.toutiao.com/api/pc/feed/?max_behot_time="+str(current_time)+"&category=__all__&utm_source=toutiao&widen=1&tadrequire=true&as=A105BD3697E7AC8&cp=5D67973A5CD88E1&_signature=Yc4bSBAXPK1ogmFdymhvcWHOG1"
    return base_url, headers, proxies
def get_response_html():
    request_url, headers, proxies = get_resquest_url_and_headers()
    response = requests.get(request_url, headers=headers, proxies=proxies)
    #声明为全局变量
    global response_json
    response_json = json.loads(response.text)

    if response_json["message"] == "error":
        get_response_html()

    return response_json

def data_to_file():
    data = response_json["data"]

    for i in range(len(data)):
        data_dict = data[i]

        with open("toutiao.json", "a+") as f:
            json.dump(data_dict, f, ensure_ascii=False)
            f.write('\n')

json_content = get_response_html()
print(json_content)
data_to_file()

import pandas as pd
df = pd.read_json("toutiao.json", lines=True)
print(df)

df.to_excel("toutiao.xlsx")

