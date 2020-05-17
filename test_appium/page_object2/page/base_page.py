import logging

import yaml
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    logging.basicConfig(level=logging.INFO)
    _black_list = [
        (MobileBy.ID, "image_cancel")
    ]
    _error_count = 0
    _error_max = 10
    _param = {}

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, locator, value=None):
        logging.info(locator)
        logging.info(value)
        try:
            return self._driver.find_element(*locator) if isinstance(locator, tuple) else self._driver.find_element(locator, value)
        except Exception as e:
            self._error_count += 1
            if self._error_count >= self._error_max:
                raise e
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    return self.find(locator, value)
                raise e

    def steps(self,file):
        with open(file,encoding="utf8") as f:
            steps:list[dict] = yaml.safe_load(f)
            element:WebElement
            for step in steps:
                logging.info(step)
                if 'by' in step.keys():
                    myby = step['by']
                    if myby == 'id':
                        element = self.find(step['by'],step['locator'])
                    if myby == 'xpath':
                        element = self.find(MobileBy.XPATH,step['locator'])
                if 'action' in step.keys():
                    action = step['action']
                    if action == 'find':
                        pass
                    if action == 'click':
                        element.click()
                    if action == 'send':
                        pass

        # if isinstance(locator, tuple):
        #     return self._driver.find_element(*locator)
        # else:
        #     return self._driver.find_element(locator, value)

