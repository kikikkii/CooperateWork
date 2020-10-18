import requests
import json
import base64
import os
from PIL import Image
from Competion import getListAPI


#获得题目，比赛用
def getQuestion(i):
    print("----------")
    url = "http://47.102.118.1:8089/api/challenge/start/"
    uuidList = getListAPI.getList()
    dict = {
        "teamid" : 3,
        "token" :"66dd62b3-6628-485d-ad2c-1f1f445382bf" 
    }
    r = requests.post(url + uuidList[i],json=dict)
    response = r.content.decode()
    #print(response)
    dict = json.loads(response)
    img_base64 = base64.b64decode(dict['data']['img'])
    file = open('.\imgtest.jpg','wb')
    file.write(img_base64)
    file.close()
    return dict
if __name__ == "__main__":
    getQuestion(1)