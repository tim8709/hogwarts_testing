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

    def test_atrr(self):
        """
        1.打开雪球首页
        2.定位首页搜索框
        3.判断搜索框是否可用，并打印搜索框name属性值
        4.打印搜索框左上角坐标和它的宽高
        5.向搜索框输入alibaba
        6.判断【阿里巴巴】是否可见
        7.如果可见，打印“搜索成功”，如果不可见，打印“搜索失败”
        """
        search = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        search_enabled = search.is_enabled()
        print(search.text)
        print(search.location)
        print(search.size)
        if search_enabled == True:
            search.click()
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
            alibaba_element = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
            # alibaba_element.is_displayed()
            element_display = alibaba_element.get_attribute("displayed")
            if element_display == "true":
                print("搜索成功")
            else:
                print("搜素失败")