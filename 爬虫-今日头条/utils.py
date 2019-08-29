import requests
import json
import random

def write_browser_info_to_file():
    my_user_agent = requests.get("https://fake-useragent.herokuapp.com/browsers/0.1.11")
    with open("browser_info.json", "w") as f:
        json.dump(my_user_agent.text, f)

#write_browser_info_to_file()

def get_random_browser():
    with open("browser_info.json", "r") as f:
        browsers_json = json.load(f)
        browsers_json = json.loads(browsers_json)
        browsers = browsers_json["browsers"]
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

        return final_browser
