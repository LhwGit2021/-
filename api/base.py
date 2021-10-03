import json
import requests

class BaseApi:
    # 实例化对象时先调用gettoken方法
    def __init__(self):
        self.wework = self.gettoken()
    # 发送请求方法
    def send_request(self, apiData):
        r = requests.request(**apiData)
        print(json.dumps(r.json(), indent=3, ensure_ascii=False))
        return r
    # 获取token方法
    def gettoken(self):
        # todo:获取 access_token
        corpid = "ww7ddf5e00dd34874c"
        corpsecret = "eChu3U03a5SUN97dNu88UHOQe9QERkwgomMUhKjBDWY"
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": corpid,
                "corpsecret": corpsecret
            }
        }
        token = self.send_request(data).json()['access_token']
        return token
