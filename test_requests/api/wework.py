from test_requests.api.base_api import BaseApi


class WeWork(BaseApi):
    corpid = "ww6feb1458237ceaee"

    def get_token(self, corpsecret):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": self.corpid,
                "corpsecret": corpsecret
            }
        }
        return self.send_api(data)["access_token"]
