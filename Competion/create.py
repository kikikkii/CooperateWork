import requests
import json

def create():
    problem = {
        "teamid": 3,
        "data": {
            "letter": "B",
            "exclude": 4,
            "challenge": [
                [0, 9, 5],
                [1, 2, 8],
                [3, 6, 7]
            ],
        "step": 8,
        "swap": [2,4]
    },
    "token": "66dd62b3-6628-485d-ad2c-1f1f445382bf"
    }
    return problem


def postcreate():
    url = "http://47.102.118.1:8089/api/challenge/create"
    headers = {
        'Accept':'text/html',
        'Content-Type': 'text/html; charset=utf-8'
    }
    #print(create())
    json_data = json.dumps(create())
    #create()
    response = requests.post(url,json=create())
    print(response.text)



if __name__ == "__main__":
    postcreate()