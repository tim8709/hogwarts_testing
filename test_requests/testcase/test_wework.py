import json

import pytest

from test_requests.api.base_api import BaseApi
from test_requests.api.tag import Tag
from test_requests.api.wework import WeWork


class TestWork:
    test_data = BaseApi.test_load("test_tag_data.yaml")
    @classmethod
    def setup_class(cls):
        cls.tag = Tag()

    @pytest.mark.parametrize("old_name,new_name", test_data)
    def test_all(self, old_name, new_name):
        data = self.tag.get_tag()
        for name in [old_name, new_name]:
            print(name)
            tag_id = self.tag.jsonpath(data, f'$..tag[?(@.name=="{name}")].id')
            if tag_id:
                self.tag.delete_tag(tag_id[0])
        assert self.tag.add_tag(old_name)["errcode"] == 0
        tag_id = self.tag.jsonpath(self.tag.get_tag(), f'$..tag[?(@.name=="{old_name}")].id')[0]
        assert self.tag.update_tag(tag_id, new_name)["errcode"] == 0

    def test_get_token(self):
        corpsecret = "neiCBsIZkMi5GlphBz_YNfeLZDgNEkyjm3SktMGfxA8"
        print(WeWork().get_token(corpsecret))

    def test_add_tag(self):
        print(self.tag.add_tag("朋友3"))

    def test_get_tag(self):
        assert self.tag.get_tag()["errcode"]==0

    def test_delete_tag(self):
        print(Tag().delete_tag("et2Gx3DAAAg7mfAdQ0GTS_Wk-fi_ioPg"))

    def test_update_tag(self):
        print(Tag().update_tag("et2Gx3DAAAT3OXcTdfPIcnDGxfX7s17w", "亲戚"))


