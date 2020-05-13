from time import sleep
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestTouchAction:
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
        pass
        # self.driver.back()
        # self.driver.quit()

    def test_atrr(self):
        action = TouchAction(self.driver)
        # action.press(x=386.5,y=1076.3).wait(200).move_to(x=386.5,y=519.5).release().perform()
        window_rect = self.driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x1 = int(width / 2)
        y_start = int(height * 4 / 5)
        y_end = int(height * 1 / 5)
        action.press(x=x1, y=y_start).wait(200).move_to(x=x1, y=y_end).release().perform()
