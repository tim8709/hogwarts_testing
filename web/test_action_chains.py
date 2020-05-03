from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(2)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_case_click(self):
        element_click = self.driver.find_element_by_id("su")
        action = ActionChains(self.driver)
        action.click(element_click)
        # action.context_click(element_click)
        # action.double_click(element_click)
        action.perform()

    @pytest.mark.skip
    def test_moveto(self):
        self.driver.get("https://www.baidu.com")
        shezhi = self.driver.find_element(By.XPATH, '//*[@id="u1"]/a[9]')
        # shezhi = self.driver.find_element_by_link_text("设置")
        action = ActionChains(self.driver)
        action.move_to_element(shezhi)
        action.perform()
        sleep(3)

    def test_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag = self.driver.find_element_by_id("dragger")
        drop1 = self.driver.find_element_by_xpath("/html/body/div[2]")
        drop2 = self.driver.find_element_by_xpath("/html/body/div[3]")
        drop3 = self.driver.find_element_by_xpath("/html/body/div[4]")
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop1).pause(1)
        action.click_and_hold(drag).release(drop2).pause(1)
        action.click_and_hold(drag).move_to_element(drop3).release().pause(1)
        action.perform()
        sleep(3)

    def test_key(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        username = self.driver.find_element_by_xpath("/html/body/label[1]/input")
        username.click()
        action = ActionChains(self.driver)
        action.send_keys("xiaoming").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("xiaohong").pause(1)
        action.send_keys(Keys.BACK_SPACE).pause(1)
        action.perform()
        sleep(3)

    def test_copy_paste(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        username1 = self.driver.find_element_by_xpath("/html/body/label[1]/input")
        username2 = self.driver.find_element_by_xpath("/html/body/label[2]/table/tbody/tr/td[2]/input")
        username1.send_keys("xiaoming")
        username1.send_keys(Keys.CONTROL, 'a')
        sleep(1)
        username1.send_keys(Keys.CONTROL, 'c')
        sleep(1)
        username2.send_keys(Keys.CONTROL, 'v')
        sleep(3)
