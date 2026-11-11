# 浏览器操作封装，供 case 目录下的脚本调用
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DriverTools:
    """selenium 浏览器基本操作封装"""

    TIMEOUT = 15

    @staticmethod
    def init_chrome():
        """初始化 Chrome 浏览器驱动"""
        return webdriver.Chrome()

    @staticmethod
    def maximize_window(driver):
        """最大化浏览器窗口"""
        driver.maximize_window()

    @staticmethod
    def open_url(driver, url):
        """打开指定页面"""
        driver.get(url)

    @staticmethod
    def click(driver, locator):
        """等待元素出现在页面上并点击，locator 为 (By.XX, "值")"""
        WebDriverWait(driver, DriverTools.TIMEOUT).until(
            EC.element_to_be_clickable(locator)
        ).click()

    @staticmethod
    def input_text(driver, locator, text):
        """等待元素可见后清空并输入内容"""
        element = WebDriverWait(driver, DriverTools.TIMEOUT).until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    @staticmethod
    def find_in_frames(driver, locator, timeout=15):
        """在主页面及所有 iframe（含嵌套）中查找可见元素，找到后 driver 停留在该 iframe 内"""
        end_time = time.time() + timeout
        while time.time() < end_time:
            driver.switch_to.default_content()
            element = DriverTools._search_frames(driver, locator)
            if element is not None:
                return element
            time.sleep(0.5)
        return None

    @staticmethod
    def _search_frames(driver, locator):
        """在当前页面递归查找元素，找不到时进入下一层 iframe 继续找"""
        for element in driver.find_elements(*locator):
            if element.is_displayed():
                return element
        for frame in driver.find_elements(By.TAG_NAME, "iframe"):
            try:
                driver.switch_to.frame(frame)
            except Exception:
                continue
            element = DriverTools._search_frames(driver, locator)
            if element is not None:
                return element
            driver.switch_to.parent_frame()
        return None
