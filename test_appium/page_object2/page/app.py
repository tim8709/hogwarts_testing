from appium import webdriver

from test_appium.page_object2.page.base_page import BasePage
from test_appium.page_object2.page.main import Main


class App(BasePage):
    def start(self):
        des_caps = {
            'platformName': 'android',
            'deviceName': '127.0.0.1:7555',
            'appPackage': 'com.tencent.wework',
            'appActivity': '.launch.WwMainActivity',
            'noReset': True
            # 'chromedriverExecutable': 'D:\workspace\hogwarts\dirver\chromedriver2.24.exe'  # 指定Chromedriver存放的位置
        }
        self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_caps)
        self._driver.implicitly_wait(10)
        return self

    def stop(self):
        pass

    def restart(self):
        pass

    def main(self):
        return Main(self._driver)