import json
import requests

#获取比赛排名接口
def getRank():
    url = "http://47.102.118.1:8089/api/rank"
    response = requests.get(url).content
    response.decode()
    dict = json.loads(response)
    for t in dict:
        print(t)


if __name__ == "__main__":
    getRank()