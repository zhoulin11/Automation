from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

caps = {}
caps["platformName"] = "Android"
caps["appium:deviceName"] = "deviceName"
caps["appium:appPackage"] = "com.tencent.mobileqq"
caps["appium:appActivity"] = "com.tencent.mobileqq.activity.SplashActivity"


driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="同意")
el1.click()
el2 = driver.find_element(by=AppiumBy.ID, value="com.tencent.mobileqq:id/btn_login")
el2.click()
el3 = driver.find_element(by=AppiumBy.ID, value="com.tencent.mobileqq:id/t3i")
el3.click()

driver.quit()