from selenium import webdriver

class TestPerformance():
    def test_performance(self):
        driver = webdriver.Chrome()
        driver.get("http://www.baidu.com")
        print(driver.execute_script("return JSON.stringify(window.performance.timing)"))