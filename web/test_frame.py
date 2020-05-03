from web.base import Base


class TestFrame(Base):
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        print(self.driver.find_element_by_id("draggable").text)
        # self.driver.switch_to.default_content()
        self.driver.switch_to.parent_frame()
        print(self.driver.find_element_by_id("submitBTN").text)
