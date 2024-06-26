# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

caps = {}
caps["platformName"] = "Android"
caps["appium:deviceName"] = "deviceName"
caps["appium:appPackage"] = "com.tencent.mobileqq"
caps["appium:appActivity"] = "com.tencent.mobileqq.activity.SplashActivity"
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 3600
caps["appium:connectHardwareKeyboard"] = True

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="同意")
el1.click()
el2 = driver.find_element(by=AppiumBy.ID, value="com.tencent.mobileqq:id/btn_login")
el2.click()
el3 = driver.find_element(by=AppiumBy.ID, value="com.tencent.mobileqq:id/t3i")
el3.click()

driver.quit()