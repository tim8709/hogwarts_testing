from time import sleep
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDW:
    def setup(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "127.0.0.1:7555",
            "platformVersion": "6.0",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "noReset": "true",
            # "dontStopAppOnReset": "true",
            "skipDeviceInitialization": "true",
            "unicodeKeyBoard": "true",
            "resetKeyBoard": "true"
        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.back()
        # self.driver.quit()

    def test_search(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()

        locator = (MobileBy.XPATH, "//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        ele = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*locator))
        # ele = self.driver.find_element(*locator)
        print(ele.text)
        current_price = float(ele.text)
        expect_price = 170
        assert current_price > expect_price

        sleep(3)
