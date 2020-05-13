from time import sleep
from appium import webdriver


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

    def test_scroll_find(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("关注")').click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable( new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("美股马甲")'
                                                        '.instance(0))').click()
        sleep(5)
