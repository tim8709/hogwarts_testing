# 滑动到浏览器底部或者顶部
# 1.打开百度页面
# 2.输入搜索关键字
# 3.点击搜索后，跳转到搜索结果页
# 4.滑动到底部点击 下一页
from time import sleep

from web.base import Base


class TestJS(Base):
    def test_js_scroll(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("selenium测试")
        self.driver.execute_script('return document.getElementById("su")').click()
        sleep(3)
        self.driver.execute_script("document.documentElement.scrollTop=2000")
        self.driver.find_element_by_xpath('//*[@id="page"]/a[10]').click()
        sleep(3)
        # for code in ['return document.title', 'return JSON.stringify(performance.timing)']:
        #     print(self.driver.execute_script(code))
        print(self.driver.execute_script('return document.title;return JSON.stringify(performance.timing)'))

    def test_datetime(self):
        self.driver.get("https://www.12306.cn/index/")
        self.driver.execute_script('a=document.getElementById("train_date");a.removeAttribute("readonly")')
        self.driver.execute_script('document.getElementById("train_date").value="2020-12-20"')
        sleep(3)
        print(self.driver.execute_script('return document.getElementById("train_date").value'))

