from time import sleep
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import *


class TestDW:
    def setup(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "127.0.0.1:7555",
            "platformVersion": "6.0",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "noReset": True,
            # "dontStopAppOnReset": True,
            "skipDeviceInitialization": True,
            "unicodeKeyBoard": "true",
            "resetKeyBoard": "true"
        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/action_close').click()
        # self.driver.back()
        # self.driver.quit()

    @pytest.mark.parametrize('searchkey,type,expect_price', [
        ('alibaba', 'BABA', 190),
        ('xiaomi', '01810', 10)
    ])
    def test_search(self, searchkey, type, expect_price):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(searchkey)
        self.driver.find_element_by_xpath(f"//*[@text='{type}']").click()

        current_price = self.driver.find_element(MobileBy.XPATH,
                                                 f"//*[@text='{type}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        current_price_float = float(current_price)
        # expect_price = 180
        assert_that(current_price_float, close_to(expect_price, expect_price * 0.2))

        sleep(3)
