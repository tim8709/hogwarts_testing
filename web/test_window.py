# 1.打开百度
# 2.点击登录-注册，输入用户名、账号
# 3.返回登录页，点击登录
# 4.输入用户名、密码，点击登录
from time import sleep

from web.base import Base


class TestWindows(Base):
    def test_window(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_link_text("登录").click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        self.driver.find_element_by_link_text("立即注册").click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("username")
        self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys("13212121212")
        sleep(3)
        self.driver.switch_to.window(windows[0])
        self.driver.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn").click()
        self.driver.find_element_by_id("TANGRAM__PSP_10__userName").send_keys("username")
        self.driver.find_element_by_id("TANGRAM__PSP_10__password").send_keys("password")
        self.driver.find_element_by_id("TANGRAM__PSP_10__submit").click()
        sleep(3)






