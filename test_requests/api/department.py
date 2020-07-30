from test_requests.api.base_api import BaseApi
from test_requests.api.wework import WeWork


class Department(BaseApi):
    corpsecret = "9W2Hetcpn03Et4PZ3PTo6VWJXESmQmc2GKZT23HrmfE"

    def __init__(self):
        self.token = WeWork().get_token(self.corpsecret)

    def add_department(self):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/department/create",
            "params": {
                "access_token": self.token
            },
            "json": {
                "name": "广州研发中心",
                "name_en": "RDGZ",
                "parentid": 1,
                "order": 1,
            }
        }
        return self.send_api(data)

    def get_department(self):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/department/list",
            "params": {
                "access_token": self.token
            },
            "json": {
                "errcode": 0,
                "errmsg": "ok",
                "department": [
                    {
                        "id": 2,
                        "name": "广州研发中心",
                        "name_en": "RDGZ",
                        "parentid": 1,
                        "order": 10
                    },
                    {
                        "id": 3,
                        "name": "邮箱产品部",
                        "name_en": "mail",
                        "parentid": 2,
                        "order": 40
                    }
                ]
            }

        }
        return self.send_api(data)

    def update_department(self):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/department/update",
            "params": {
                "access_token": self.token
            },
            "json": {
                "id": 3,
                "name": "广州研发中心",
                "name_en": "RDGZ",
                "parentid": 1,
            }
        }
        return self.send_api(data)

    def delete_department(self):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/department/delete",
            "params": {
                "access_token": self.token,
                "id": 3
            }
        }
        return self.send_api(data)


if __name__ == '__main__':
    # Department().add_department()
    # Department().get_department()
    # Department().update_department()
    Department().delete_department()
