from test_appium.page_object.page.base_page import BasePage


class Search(BasePage):
    def search(self,value):
        self._params["value"] = value
        self.steps("../page/search.yaml")