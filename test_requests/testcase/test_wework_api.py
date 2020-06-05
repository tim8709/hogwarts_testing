import requests


class TestWeworkApi:
    corpid = "ww6feb1458237ceaee"
    corpsecret = "9W2Hetcpn03Et4PZ3PTo6VWJXESmQmc2GKZT23HrmfE"

    def setup(self):
        res = requests.get(
            f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={self.corpid}&corpsecret={self.corpsecret}")
        self.token = res.json()["access_token"]
        print(self.token)

    def test_wework_api(self):
        # 读取用户
        get_user_info = requests.get(
            f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid=CeShi01")
        print(get_user_info.json())
        # 若用户存在，则删除此用户
        if get_user_info.json()["errcode"] == 0:
            requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid=CeShi01")
        # 删除用户后，再创建用户
        create_data = {
            "userid": "addUser2",
            "name": "用户2",
            "mobile": "15800000003",
            "department": [1]
        }
        add_user = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}",
                                 json=create_data)
        print(add_user.json())
        # 创建用户后，修改用户信息
        update_data = {
            "userid": "addUser2",
            "name": "用户3"
        }
        update_user_info = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}",
                                         json=update_data)
        print(update_user_info.json())
