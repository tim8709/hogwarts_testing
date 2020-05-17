from appium import webdriver
from time import sleep


class TestBrowser():
    def setup(self):
        des_caps = {
            'platformName': 'android',
            'platformVersion': '6.0',
            'browserName': 'Browser',
            'noRest': True,
            'deviceName': '127.0.0.1:7555',
            'chromedriverExecutable': 'D:\workspace\hogwarts\dirver\chromedriver2.24.exe'  # 指定Chromedriver存放的位置
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        # self.driver.quit()
        pass

    def test_browser(self):
        self.driver.get("http://www.baidu.com")
        sleep(5)
