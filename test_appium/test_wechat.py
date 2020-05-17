from time import sleep
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestBrowser():

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

    # def setup(self):
    #     pass
    #
    # def teardown(self):
    #     self.driver.back()

    # @pytest.fixture()
    # def add_fixture(self):
    #     yield
    #     self.driver.back()

    @pytest.mark.parametrize('name,gender,phone', [
        ('姓名16', '男', '13200000016'),
        ('姓名17', '男', '13200000017')
    ])
    def test_add_member(self, add_fixture, name, gender, phone):
        # name = "姓名6"
        # gender = "男"
        # phone = "13211111116"
        # 进入通讯录
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        # 滚动查找“添加成员”
        self.driver.find_element_by_android_uiautomator('new UiScrollable( new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("添加成员")'
                                                        '.instance(0))').click()
        # 手动添加
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/c7g").click()

        current_act = self.driver.current_activity
        assert ".contact.controller.ContactAddActivity" in current_act

        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"姓名")]/../*[@text="必填"]').send_keys(name)
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/dux').click()
        sleep(1)
        if gender == "男":
            self.driver.find_element(MobileBy.XPATH, '//*[@text="男"]').click()
        else:
            self.driver.find_element(MobileBy.XPATH, '//*[@text="女"]').click()

        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/eq7').send_keys(phone)
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/gur').click()
        sleep(1)
        # print(self.driver.page_source)
        assert "添加成功" in self.driver.find_element(MobileBy.XPATH, '//*[@text="添加成功"]').text

    @pytest.mark.parametrize('name', [
        '姓名5', '姓名7'
    ])
    def test_delete_member(self, name):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        self.driver.find_element(MobileBy.XPATH, f'//*[@text="{name}"]').click()
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/guk').click()
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/azd').click()
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/duq').click()
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/b_4').click()
        sleep(3)
        deleted_member = self.driver.find_elements(MobileBy.XPATH, f'//*[@text="{name}"]')
        assert len(deleted_member) == 0

    def test_delete_member2(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        while True:
            members = self.driver.find_elements(MobileBy.XPATH, '//*[contains(@text,"姓名")]')
            if len(members) ==0:
                print("没有要删除的成员了")
                break
            text = members[0].text
            members[0].click()
            self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/guk').click()
            self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/azd').click()
            self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/duq').click()
            self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/b_4').click()
            sleep(3)
            assert text not in self.driver.page_source
