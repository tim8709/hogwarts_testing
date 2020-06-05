from unittest import TestCase
from test_http import test_demo

class TestApiRequest(TestCase):
    def test_send(self):
        ar = test_demo.ApiRequest()
        ar.send()
