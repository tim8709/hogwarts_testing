from time import sleep

from selenium import webdriver
from selenium.webdriver import TouchActions


class TestTouchAction():
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_touchaction_scrollbotton(self):
        self.driver.get("https://www.baidu.com")
        el = self.driver.find_element_by_id("kw")
        el_search = self.driver.find_element_by_id("su")
        el.send_keys("selenium 测试")
        action = TouchActions(self.driver)
        action.tap(el_search)
        action.scroll_from_element(el, 0, 1000)
        action.perform()
        sleep(3)
