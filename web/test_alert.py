from time import sleep

from selenium.webdriver import ActionChains

from web.base import Base


class TestAlert(Base):
    """
    1.打开网页 https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable
    2.拖拽元素A到元素B
    3.此时会有alert弹窗，点击确定
    4.点击运行
    5.关闭网页
    """

    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        drag = self.driver.find_element_by_id("draggable")
        drop = self.driver.find_element_by_id("droppable")
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop).perform()
        sleep(3)
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath('//*[@id="submitBTN"]').click()
        sleep(3)
