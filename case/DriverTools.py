import pytest
import time
from appium import webdriver
from page import LoginPage

caps = {}
caps["platformName"] = "Android"
caps["appium:deviceName"] = "deviceName"
caps["appium:appPackage"] = "com.tencent.mobileqq"
caps["appium:appActivity"] = "com.tencent.mobileqq.activity.SplashActivity"
class Test_project:
    # 进入登录页面
    @pytest.mark.skip(reason="功能未实现")
    # @pytest.mark.run(order=1)
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
    @pytest.mark.skip(reason="功能未实现")
    # @pytest.mark.run(order=2)
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
    #输入用户名、密码登录
    # @pytest.mark.skip(reason="功能未实现")
    @pytest.mark.skip(reason="功能未实现")
    # @pytest.mark.run(order=3)
    # @pytest.mark.parametrize("user,passwd",[[2377335189,"gzdxzl3301"],[1419310155,"gzdxzl3302"]])
    def test_003(self, user,passwd):
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        driver.find_element_by_accessibility_id("同意").click()
        time.sleep(3)
        driver.find_element_by_id("com.tencent.mobileqq:id/btn_login").click()
        time.sleep(3)
        driver.find_element_by_id("com.tencent.mobileqq:id/t3i").click()
        time.sleep(3)
        driver.find_element_by_accessibility_id("请输入QQ号码或手机号或QID或邮箱").send_keys(user)
        driver.find_element_by_id("com.tencent.mobileqq:id/tsd").send_keys(passwd)
        driver.find_element_by_accessibility_id("同意协议").click()
        driver.find_element_by_accessibility_id("登录").click()
        titles = driver.find_elements_by_id("com.tencent.mobileqq:id/ivTitleName")
        for title in titles:
            text = title.get_attribute("text")
            sorted(text) == sorted('安全验证')
        time.sleep(3)
        driver.quit()

    def test_004(self):
        login_page = BasePage.LoginPage(self.driver)


