import requests
import json
import base64
import os
from PIL import Image
# -*- coding: utf-8 -*-

def request():
    print("------------------")
    r = requests.get('http://47.102.118.1:8089/api/problem?stuid=031802615 ')
    print("--------------")
    #print(r.json())
    #得到r.json格式
    response = r.content.decode()
    #print(response)
    dict = json.loads(response)
    img_base64 = base64.b64decode(dict['img'])
    #print(img_base64)
    #桌面的位置C:\Users\lbh\Desktop
    file = open('.\imgtest.jpg','wb')
    file.write(img_base64)
    file.close()
    return dict

def post(uuid,operations,swap):
    url = "http://47.102.118.1:8089/api/answer"
    data = {"uuid" : "c6fb77dae95f4bc8b6d3a5b54a293a62",
            "answer" : {
                "operations": "wsaaadasdadadaws",
                "swap": [1,2]
                }
            }
    print(data)
    js = json.dumps(data)
    print(js)
    res = requests.post(url=url,data = js,headers={'Content-Type': 'application/json'})
    print(res.json())
    print(res.status_code)

if __name__ == "__main__":
    post(1,1,1)



