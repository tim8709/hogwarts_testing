from selenium import webdriver


class BasePage():
    _base_url = ""

    def __init__(self, driver: webdriver = None):
        # self._driver = None
        # # 如果没有传driver，则初始化driver
        # if driver is None:
        #     self._driver = webdriver.Chrome(r"D:\workspace\hogwarts\dirver\chromedriver.exe")
        # # 否则复用已有的driver
        # else:
        #     self._driver = driver
        # if self._base_url != "":
        #     self._driver.get(self._base_url)

        self.driver = None
        if driver is None:
            # 开启本地9222端口调试
            self.chrome_opts = webdriver.ChromeOptions()
            self.chrome_opts.debugger_address = "172.0.0.1:9222"
            self.driver = webdriver.Chrome(options=self.chrome_opts)
            # 浏览器最大化
            self.driver.maximize_window()
            # 隐式等待
            self.driver.implicitly_wait(3)
        else:
            self.driver = driver

    def find(self, by, locator):
        return self.driver.find_element(by, locator)
