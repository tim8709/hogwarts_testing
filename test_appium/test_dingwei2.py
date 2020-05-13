from time import sleep
from appium import webdriver


class TestDW:
    def setup(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "127.0.0.1:7555",
            "platformVersion": "6.0",
            # "appPackage": "com.xueqiu.android",
            # "appActivity": ".view.WelcomeActivityAlias",
            "noReset": "true",
            "dontStopAppOnReset": "true",
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
        """
        1.打开雪球app
        2.点击搜索输入框
        3.搜索输入框输入“阿里巴巴”
        4.搜索结果中选择“阿里巴巴”并点击
        5.获取阿里巴巴的股价，并判断价格>200
        """
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        current_price = float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
        assert current_price > 200

        sleep(3)
