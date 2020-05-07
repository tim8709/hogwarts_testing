from selenium.webdriver.common.by import By

from web.selenium.page.base_page import BasePage


class AddMember(BasePage):
    def add_member(self):
        self.find(By.ID, "username").send_keys("姓名")
        self.find(By.ID, "memberAdd_acctid").send_keys("zhanghao")
        self.find(By.ID, "memberAdd_phone").send_keys("13211111111")
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()

    def get_member_names(self):
        # return self.finds(By.CSS_SELECTOR, ".js_list tr:nth-child(2) td:nth-child(2)").get_attribute("title")
        name_list = []
        names = self.finds(By.CSS_SELECTOR, "#member_list td:nth-child(2)")
        for name in names:
            name_list.append(name.get_attribute("title"))
        return name_list
