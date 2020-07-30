import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestSendMessage():

    def setup_class(self):
        des_caps = {
            'platformName': 'android',
            'deviceName': '127.0.0.1:7555',
            'appPackage': 'com.tencent.wework',
            'appActivity': '.launch.WwMainActivity',
            'noReset': True,
            'chromedriverExecutable': 'D:\workspace\hogwarts\dirver\chromedriver2.24.exe'  # 指定Chromedriver存放的位置
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_caps)
        self.driver.implicitly_wait(10)

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.parametrize('name,message', [
        ('user1', '你好'),
        ('user2', '他好')
    ])
    def test_add_member(self, name, message):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        self.driver.find_element_by_id("com.tencent.wework:id/guu").click()
        self.driver.find_element_by_id("com.tencent.wework:id/fk1").send_keys(f'{name}')
        self.driver.find_element_by_id("com.tencent.wework:id/dqe").click()
        self.driver.find_element_by_id("com.tencent.wework:id/abo").click()
        self.driver.find_element_by_id('com.tencent.wework:id/dx1').send_keys(f"{message}")
        self.driver.find_element_by_id("com.tencent.wework:id/dwx").click()
