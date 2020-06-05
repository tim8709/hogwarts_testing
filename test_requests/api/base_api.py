from pprint import pprint
from string import Template

import requests
import yaml
from jsonpath import jsonpath


class BaseApi:
    def send_api(self, req: dict):
        pprint(req)
        r = requests.request(**req)
        pprint(r.json())
        return r.json()

    @classmethod
    def jsonpath(cls, json, expr):
        return jsonpath(json, expr)

    @classmethod
    def test_load(cls, file):
        with open(file, "r", encoding="utf8") as f:
            return yaml.safe_load(f)

    @classmethod
    def template(cls,path,data):
        with open(path,'r',encoding="utf8") as f:
            return yaml.load(Template(f.read()).substitute(data))
