from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from test_appium.page_object2.page.base_page import BasePage



class ContactAddPage(BasePage):
    def input_name(self, name):
        self.find(MobileBy.XPATH, '//*[contains(@text,"姓名")]/../*[@text="必填"]').send_keys(name)
        return self

    def set_gender(self, gender):
        self.find(MobileBy.ID, 'com.tencent.wework:id/dux').click()
        sleep(1)
        if gender == "男":
            self.find(MobileBy.XPATH, '//*[@text="男"]').click()
        else:
            self.find(MobileBy.XPATH, '//*[@text="女"]').click()
        return self

    def input_phone(self, phone):
        self.find(MobileBy.ID, 'com.tencent.wework:id/eq7').send_keys(phone)
        return self

    def click_save(self):
        from test_appium.page_object2.page.member_Invite_page import MemberInvitePage
        self.find(MobileBy.ID, 'com.tencent.wework:id/gur').click()
        return MemberInvitePage(self._driver)
