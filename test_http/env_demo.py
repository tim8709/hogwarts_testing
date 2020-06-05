import requests
import yaml

'''
请求之前，对请求的url进行替换
1.需要二次封装requests，对请求进行定制化
2.将请求结构体的url从一个写死的ip地址改为任意的域名
3.使用env配置文件，存放各环境的配置信息
4.将请求结构体中的url替换为env配置文件中个人选择的url
5.将env配置文件使用yaml进行管理
'''


class Api:
    data = {
        "method": "get",
        "url": "http://localhost:9999/demo.txt",
        "headers": None
    }

    env = yaml.safe_load(open("env.yaml"))

    def send(self, data: dict):
        data["url"] = str(data["url"]).replace("localhost", self.env["list"][self.env["default"]])
        r = requests.request(method=data["method"], url=data["url"], headers=data["headers"])
