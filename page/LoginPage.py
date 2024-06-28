import time
from appium import webdriver
from BasePage import BasePage

class LoginPage(BasePage):
    def set_username(self, username):
        name = self.driver.find_element_by_accessibility_id("请输入QQ号码或手机号或QID或邮箱")
        name.send_keys(username)
    def set_password(self, password):
        pwd = self.driver.find_element_by_id("com.tencent.mobileqq:id/tsd")
        pwd.send_keys(password)
    def click_Ggreement(self):
        Ggreement = self.driver.find_element_by_accessibility_id("同意协议")
        Ggreement.click()
    def click_Login(self):
        Login = self.driver.find_element_by_accessibility_id("登录")
        Login.click()