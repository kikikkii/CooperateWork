import requests
import json

def getList():
    url = "http://47.102.118.1:8089/api/challenge/list"
    r = requests.get(url)
    print("-------------------")
    response = r.content.decode()
    dict = json.loads(response)
    uuidList = []
    for t in dict:
        uuidList.append(t['uuid'])
        #print(t)
        
    return uuidList



if __name__ == "__main__":
    getList()