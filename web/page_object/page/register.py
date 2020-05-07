from selenium.webdriver.common.by import By

from web.page_object.page.base_page import BasePage


class Register(BasePage):
    # 填写表单
    def register(self):
        self.find(By.ID, "corp_name").send_keys("hello")
        self.find(By.ID, "manager_name").send_keys("hello2")
        # return self.find().get_attribute("xxx")
        return True

