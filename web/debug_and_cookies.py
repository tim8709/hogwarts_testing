import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestDebug():
    def setup(self):
        # 声明一个变量，设置为chrometoptions
        chrome_opts = webdriver.ChromeOptions()
        # 此处的端口号要与chrome调试模式设置的端口号相同
        chrome_opts.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=chrome_opts)
        self.driver.get("https://work.weixin.qq.com")

    def teardown(self):
        # self.driver.quit()
        pass

    def test_debug(self):
        # self.driver.get("https://home.testing-studio.com/")
        self.driver.find_element(By.CSS_SELECTOR, ".ww_icon_AppMemberJoinBig").click()

    def test_cookies(self):
        # sleep(15)
        # cookies = self.driver.get_cookies()
        # with open("cookies.txt", "w") as f:
        #     json.dump(cookies, f)
        with open("cookies.txt", "r") as f:
            cookies = json.load(f)
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element_by_css_selector(".index_service_cnt_itemWrap:nth-child(1)").click()
