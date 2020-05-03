from time import sleep

from web.base import Base


class TestFile(Base):
    def test_file_upload(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_xpath('//*[@id="sttb"]/img[1]').click()
        self.driver.find_element_by_id("stfile").send_keys(r"C:\Users\xx\Desktop\截图.png")
        sleep(3)
