from time import sleep

from selenium.webdriver.common.by import By

from web.selenium.page.add_member import AddMember
from web.selenium.page.base_page import BasePage


class Index(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def goto_add_member(self):
        # self.find(By.CSS_SELECTOR, ".index_service_cnt_item").click()
        self.find(By.ID, "menu_contacts").click()

        def wait():
            ele_len = len(self.finds(By.ID, "username"))
            if ele_len < 1:
                self.find(By.CSS_SELECTOR, ".js_has_member>div:nth-child(1) .js_add_member").click()
            # 如果username存在，则返回True
            # 如果useranme不存在，则返回False
            return ele_len >= 1
        self.wait_for(wait)
        return AddMember(reuse=True)
