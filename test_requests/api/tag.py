from test_requests.api.base_api import BaseApi
from test_requests.api.wework import WeWork


class Tag(BaseApi):
    corpsecret = "neiCBsIZkMi5GlphBz_YNfeLZDgNEkyjm3SktMGfxA8"

    def __init__(self):
        self.token = WeWork().get_token(self.corpsecret)

    def add_tag(self,name):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
            "params": {
                "access_token": self.token
            },
            "json": {
                "group_name": "关系",
                "tag": [{
                    "name": name,
                }
                ]
            }
        }
        return self.send_api(data)

    def get_tag(self):
        # data = self.test_load("tag_get.yaml")
        # data["params"]["access_token"] = self.token
        data = self.template('tag_get.yaml',{'access_token':self.token})
        return self.send_api(data)

    def delete_tag(self, tagId):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            "params": {
                "access_token": self.token
            },
            "json": {
                "tag_id": [
                    tagId
                ]
            }
        }
        return self.send_api(data)

    def update_tag(self,id,name):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag",
            "params": {
                "access_token": self.token
            },
            "json": {
                "id": id,
                "name": name
            }
        }
        return self.send_api(data)
