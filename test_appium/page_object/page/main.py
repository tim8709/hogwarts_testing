from test_appium.page_object.page.base_page import BasePage
from test_appium.page_object.page.market import Market


class Main(BasePage):
    def goto_market(self):
        self.steps("../page/main.yaml")
        return Market(self._driver)