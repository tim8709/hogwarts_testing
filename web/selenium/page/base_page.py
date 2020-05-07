from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    # 把driver提取出来
    _driver = ""
    base_url = ""

    def __init__(self, reuse=False):
        # 如果driver等于True，则复用已有的浏览器
        if reuse == True:
            opts = webdriver.ChromeOptions()
            opts.debugger_address = "127.0.0.1:9222"
            self._driver = webdriver.Chrome(options=opts)
        else:
            # 否则新打开浏览器
            self._driver = webdriver.Chrome()
        if self.base_url != "":
            self._driver.get(self.base_url)
        self._driver.implicitly_wait(3)

    def find(self, by, locator):
        return self._driver.find_element(by, locator)

    def finds(self, by, locator):
        return self._driver.find_elements(by, locator)

    def wait_for(self, func):
        WebDriverWait(self._driver, 10).until(func)
