import requests
import json
from jsonschema import validate
from requests.auth import HTTPBasicAuth
import base64


class TestDemo:
    def test_get(self):
        r = requests.get("http://httpbin.org/get")
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200

    def test_query(self):
        payload = {'key1': 'value1', 'key2': 'value2'}
        r = requests.get('http://httpbin.org/get', params=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post_form(self):
        payload = {'key1': 'value1', 'key2': 'value2'}
        r = requests.post('http://httpbin.org/post', data=payload)
        print(r.text)
        assert r.status_code == 200

    def test_header(self):
        r = requests.get('http://httpbin.org/get', headers={"h": "header demo"})
        print(r.json())
        assert r.status_code == 200
        assert r.json()['headers']['H'] == "header demo"

    def test_post_json(self):
        payload = {'key1': 1, 'key2': 'value2'}
        r = requests.post('http://httpbin.org/post', json=payload)
        print(r.text)
        assert r.status_code == 200
        assert r.json()['json']['key1'] == 1

    def test_get_login_jsonschema(self):
        url = "https://xxxx"
        data = requests.get(url, params={'limit': '2'}).json()
        schema = json.loads(open("topic_schema.json"))
        validate(data, schema=schema)

    def test_header_cookie(self):
        url = "http://httpbin.org/cookies"
        header = {"Cookie": "nihao"}  # 注：Cookie首字母须大写，末尾没有s
        r = requests.get(url=url, headers=header)
        print(r.request.headers)

    def test_cookies(self):
        url = "http://httpbin.org/cookies"
        cookies_data = {"cookies": "nihao",
                        "cookies2": "hello"
                        }
        r = requests.get(url=url, cookies=cookies_data)
        print(r.request.headers)

    def test_auth(self):
        r = requests.get(url="http://httpbin.org/basic-auth/root/123",
                         auth=HTTPBasicAuth("root", "123"))
        print(r.text)

    def test_encode(self):
        url = "http://localhost:9999/demo.txt"
        r = requests.get(url=url)
        res = json.loads(base64.b64decode(r.content))
        print(res)


class ApiRequest:
    req_data = {
        "method": "get",
        "url": "http://localhost:9999/demo.txt",
        "headers": None,
        "encoding": "base64"
    }

    def send(self, data: dict):
        res = requests.request(data["method"], data["url"], headers=data["headers"])
        if data["encoding"] == "base64":
            return json.loads(base64.b64decode(res.content))
        # 把加密后的响应发给第三方服务，让第三方做解密然后返回解密后的信息
        elif data["encoding"] == "private":
            return requests.post("url",data=res.content)
