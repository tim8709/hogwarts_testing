from selenium.webdriver.common.by import By

from web.page_object.page.base_page import BasePage
from web.page_object.page.login import Login
from web.page_object.page.register import Register


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/"

    def goto_register(self):
        self.find(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        return Register(self._driver)

    def goto_login(self):
        self.find(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        return Login(self._driver)
