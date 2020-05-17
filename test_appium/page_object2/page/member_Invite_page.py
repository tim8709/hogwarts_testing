# from test_appium.page_object2.page.address_list_page import AddressListPage
from appium.webdriver.common.mobileby import MobileBy

from test_appium.page_object2.page.base_page import BasePage
# from test_appium.page_object2.page.contact_add_page import ContactAddPage


class MemberInvitePage(BasePage):
    def click_addmanully(self):
        from test_appium.page_object2.page.contact_add_page import ContactAddPage
        self.find(MobileBy.ID, "com.tencent.wework:id/c7g").click()
        return ContactAddPage(self._driver)

    def click_back(self):
        from test_appium.page_object2.page.address_list_page import AddressListPage
        return AddressListPage(self._driver)

    def veriy_toast(self):
        self.find(MobileBy.XPATH, '//*[@text="添加成功"]')
        return self