from appium.webdriver.common.mobileby import MobileBy

from test_appium.page_object2.page.base_page import BasePage
from test_appium.page_object2.page.address_list_page import AddressListPage


class Main(BasePage):
    def goto_message(self):
        pass

    def goto_addresslist(self):
        self.find(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        self.steps("../steps/mainsteps.yml")
        return AddressListPage(self._driver)

    def goto_workbench(self):
        pass

    def goto_profile(self):
        pass