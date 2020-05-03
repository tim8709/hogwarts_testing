from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestHogwarts():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_selenium(self):
        self.driver.get("http://www.testerhome.com")
        self.driver.find_element_by_link_text("社团").click()
        self.driver.find_element_by_link_text("霍格沃兹测试学院").click()

    # def test_wait(self):
    #     def wait(x):
    #         return len(self.driver.find_elements(By.XPATH, '//*[@class="table-heading"]')) >= 1
    #
    #     WebDriverWait(self.driver, 10).until(wait)

    def test_wait(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(By.XPATH,'//xx'))
        self.driver.find_elements(By.XPATH, 'xx...').click()
