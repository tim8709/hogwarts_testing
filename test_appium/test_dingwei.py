from time import sleep

from appium import webdriver

desired_caps = {
    "platformName": "Android",
    "deviceName": "127.0.0.1:7555",
    "platformVersion": "6.0",
    "appPackage": "com.xueqiu.android",
    "appActivity": ".view.WelcomeActivityAlias",
    "noReset": "true",
    "dontStopAppOnReset": "true",
    "skipDeviceInitialization": "true"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)
driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
driver.find_element_by_accessibility_id("content-desc")
driver.back()
driver.back()
sleep(3)
driver.quit()
