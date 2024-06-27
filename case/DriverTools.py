import pytest
import time
from appium import webdriver

caps = {}
caps["platformName"] = "Android"
caps["appium:deviceName"] = "deviceName"
caps["appium:appPackage"] = "com.tencent.mobileqq"
caps["appium:appActivity"] = "com.tencent.mobileqq.activity.SplashActivity"
class Test_project:
    # 进入登录页面
    @pytest.mark.run(order=1)
    def test_001(self):
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        app = driver.find_element_by_accessibility_id("同意").click()
        time.sleep(3)
        app = driver.find_element_by_id("com.tencent.mobileqq:id/btn_login").click()
        time.sleep(3)
        app = driver.find_element_by_id("com.tencent.mobileqq:id/t3i").click()
        time.sleep(3)
        titles = driver.find_elements_by_id("com.tencent.mobileqq:id/t3i")
        for title in titles:
            classname = title.get_attribute("className")
            sorted(classname) == sorted('android.widget.ImageView')
        driver.quit()
    # 进入注册页面
    @pytest.mark.run(order=2)
    def test_002(self):
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        time.sleep(3)
        app2 = driver.find_element_by_accessibility_id("同意").click()
        time.sleep(3)
        app2 = driver.find_element_by_id("com.tencent.mobileqq:id/btn_register").click()
        time.sleep(3)
        titles = driver.find_elements_by_id("com.tencent.mobileqq:id/f8w")
        for title in titles:
            text = title.get_attribute("text")
            sorted(text) == sorted('同意并继续')
        driver.quit()


