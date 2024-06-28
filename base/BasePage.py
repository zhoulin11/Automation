class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.find_element_by_accessibility_id("同意").click()
        time.sleep(3)
        self.driver.find_element_by_id("com.tencent.mobileqq:id/btn_login").click()
        time.sleep(3)
        self.driver.find_element_by_id("com.tencent.mobileqq:id/t3i").click()
        time.sleep(3)