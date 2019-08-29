'''
请求地址
https://www.toutiao.com/api/pc/feed/?
max_behot_time=1567044847&
category=__all__&
utm_source=toutiao&
widen=1&tadrequire=true&
as=A155BDA65796AA7&
cp=5D67168A0A279E1&
_signature=Yc4bSBAXPK1ogmFdymincGHOG1
'''
import time
import requests
import json
import random

def get_one_user_agent():
    my_user_agent = requests.get("https://fake-useragent.herokuapp.com/browsers/0.1.11")
    agent_json = json.loads(my_user_agent.text)
    browsers = agent_json["browsers"]
    #随机一个浏览器类型
    i = random.randint(0, len(browsers))
    browser_name = ""
    if i == 0:
        browser_name = "chrome"
    elif i == 1:
        browser_name = "opera"
    elif i == 2:
        browser_name = "firefox"
    elif i == 3:
        browser_name = "internetexplorer"
    else:
        browser_name = "safari"
    final_browser = browsers[browser_name][random.randint(0, len(browsers[browser_name]))]
    #print(final_browser)

user_agent = get_one_user_agent()
current_time = int(time.time())
#发起请求
proxies = {
    "url":"https://125.110.89.147:9000"
}
headers = {
    "user-agent":user_agent
}
response = requests.get(url='https://www.toutiao.com/api/pc/feed/?'
                            'max_behot_time=1567037917 &'
                            'category=__all__&'
                            'utm_source=toutiao&'
                            'widen=1&'
                            'tadrequire=true&'
                            'as=A1D5FD5647B6AFC&cp=5D67068AAF9CBE1&_signature=Yc4bSBAXPK1ogmFdymgDyGHOG1'
                        ,headers=headers, proxies=proxies)

#print(response.text.encode("utf-8").decode("unicode-escape"))

