from test_appium.page_object.page.base_page import BasePage
from test_appium.page_object.page.search import Search


class Market(BasePage):
    def goto_search(self):
        self.steps("../page/market.yaml")
        return Search(self._driver)