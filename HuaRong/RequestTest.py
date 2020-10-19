import requests
import json
import base64
import os
from PIL import Image
# -*- coding: utf-8 -*-

#request函数，正常题目用
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


#post函数
def post(board):
    #题目用
    url = "http://47.102.118.1:8089/api/answer"
    
    #题目用数据
    data = {
        "uuid":board.uuid,
        "answer":{
            "operations":board.operates,
            "swap": board.change
       }
    }
    """
    #比赛用
    #url = 'http://47.102.118.1:8089/api/challenge/submit'

    data = {"uuid" : board.uuid,
            "teamid":3,
            "token":"66dd62b3-6628-485d-ad2c-1f1f445382bf",
            "answer" : {
                "operations": board.operates,
                "swap": board.change
                }
            }
    """
    print(data)
    js = json.dumps(data)
    print(js)
    res = requests.post(url=url,data = js,headers={'Content-Type': 'application/json'})
    print(res.json())
    print(res.status_code)


if __name__ == "__main__":
    post(1,1,1)

"""{
    "uuid": "ac09e60d-4089-44d6-94af-xxxxxxx",
    "teamid": 2,
    "token": "123123",
    "answer": {
        "operations": "d",
        "swap": []
    }
}"""

