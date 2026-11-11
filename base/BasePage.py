"""Selenium 基础操作封装：页面操作、元素查找、元素操作、iframe 处理"""
import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """所有页面对象的父类，提供统一的元素操作能力"""

    # 默认显式等待超时时间（秒）
    DEFAULT_TIMEOUT = 10
    # 默认轮询间隔（秒）
    POLL_FREQUENCY = 0.5

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.DEFAULT_TIMEOUT, self.POLL_FREQUENCY)

    # ==================== 页面操作 ====================
    def open_url(self, url):
        """打开指定页面"""
        self.driver.get(url)

    def maximize_window(self):
        """最大化浏览器窗口"""
        self.driver.maximize_window()

    def get_title(self):
        """获取当前页面标题"""
        return self.driver.title

    def get_current_url(self):
        """获取当前页面地址"""
        return self.driver.current_url

    def wait_title_not_contains(self, text, timeout=60):
        """等待标题不再包含指定文本，用于判断页面跳转完成"""
        try:
            WebDriverWait(self.driver, timeout, self.POLL_FREQUENCY).until(
                lambda d: text not in d.title
            )
            return True
        except TimeoutException:
            return False

    # ==================== 元素查找 ====================
    def find_element(self, locator: tuple):
        """查找单个元素（只要存在于 DOM 中）"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator: tuple):
        """查找多个元素"""
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def find_visible_element(self, locator: tuple):
        """查找可见的元素"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_clickable_element(self, locator: tuple):
        """查找可点击的元素"""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find_in_frames(self, locator: tuple, timeout=None):
        """在主页面及所有 iframe（含嵌套）中查找可见元素，找到后 driver 停留在该 iframe 内"""
        end_time = time.time() + (timeout or self.DEFAULT_TIMEOUT)
        while time.time() < end_time:
            self.switch_to_default_content()
            element = self._search_frames(locator)
            if element is not None:
                return element
            time.sleep(self.POLL_FREQUENCY)
        raise TimeoutException(f"在页面及 iframe 中均未找到元素：{locator}")

    def _search_frames(self, locator: tuple):
        """在当前页面递归查找元素，找不到时进入下一层 iframe 继续找"""
        for element in self.driver.find_elements(*locator):
            if element.is_displayed():
                return element
        for frame in self.driver.find_elements(By.TAG_NAME, "iframe"):
            try:
                self.driver.switch_to.frame(frame)
            except Exception:
                continue
            element = self._search_frames(locator)
            if element is not None:
                return element
            self.driver.switch_to.parent_frame()
        return None

    # ==================== 元素操作 ====================
    def click(self, locator: tuple):
        """点击元素"""
        self.find_clickable_element(locator).click()

    def click_element(self, element):
        """点击已定位的元素，被遮挡时用 JS 点击兜底"""
        try:
            element.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", element)

    def input_text(self, locator: tuple, text: str, clear_first=True):
        """在输入框中输入文本"""
        self.input_element(self.find_visible_element(locator), text, clear_first)

    def input_element(self, element, text, clear_first=True):
        """向已定位的输入元素输入文本"""
        if clear_first:
            element.clear()
        element.send_keys(text)

    def get_text(self, locator: tuple):
        """获取元素文本"""
        return self.find_visible_element(locator).text

    def get_attribute(self, locator: tuple, attribute: str):
        """获取元素属性值"""
        return self.find_element(locator).get_attribute(attribute)

    # ==================== 状态判断 ====================
    def is_element_present(self, locator: tuple, timeout=5):
        """判断元素是否存在"""
        try:
            WebDriverWait(self.driver, timeout, self.POLL_FREQUENCY).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def is_element_visible(self, locator: tuple, timeout=5):
        """判断元素是否可见"""
        try:
            WebDriverWait(self.driver, timeout, self.POLL_FREQUENCY).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    # ==================== frame 切换 ====================
    def switch_to_default_content(self):
        """回到主文档"""
        self.driver.switch_to.default_content()
