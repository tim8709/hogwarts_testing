import yaml

from test_requests.api.base_api import BaseApi


def test_load():
    with open("test_tag_data.yaml","r",encoding="utf8") as f:
        return yaml.safe_load(f)
        # print(yaml.safe_load(f))

def test_template():
    print(BaseApi.template("tag_get.yaml", {"access_token": 123}))