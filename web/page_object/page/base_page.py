from selenium import webdriver


class BasePage():
    _base_url = ""

    def __init__(self, driver: webdriver = None) -> bool:
        self._driver = ""
        if driver is None:
            self._driver = webdriver.Chrome(r"D:\workspace\hogwarts\dirver\chromedriver.exe")
        else:
            self._driver = driver
        if self._base_url != "":
            self._driver.get(self._base_url)

    def find(self, by, locator):
        return self._driver.find_element(by, locator)
