from appium.webdriver.common.mobileby import MobileBy

from test_appium.page_object2.page.base_page import BasePage
# from test_appium.page_object2.page.member_Invite_page import MemberInvitePage


class AddressListPage(BasePage):
    def click_addmember(self):
        from test_appium.page_object2.page.member_Invite_page import MemberInvitePage
        self.find(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable( new UiSelector().'
                                                'scrollable(true).instance(0)).'
                                                'scrollIntoView(new UiSelector().text("添加成员")'
                                                '.instance(0))').click()
        return MemberInvitePage(self._driver)