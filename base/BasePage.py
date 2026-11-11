import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
class BasePage:
    """Selenium 基础操作封装类"""
    # 默认超时时间（秒）
    DEFAULT_TIMEOUT = 10
    # 默认轮询间隔（秒）
    DEFAULT_POLL_FREQUENCY = 0.5
    def __init__(self, driver: webdriver.Chrome):
        """
        初始化 BasePage
        :param driver: WebDriver 实例
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, self.DEFAULT_TIMEOUT, self.DEFAULT_POLL_FREQUENCY)
    # ==================== 元素定位 ====================
    def find_element(self, locator: tuple):
        """
        查找单个元素（带显式等待）
        :param locator: 定位器，格式为 (By.ID, 'value') 等
        :return: WebElement
        """
        return self.wait.until(EC.presence_of_element_located(locator))
    def find_elements(self, locator: tuple):
        """
        查找多个元素（带显式等待）
        :param locator: 定位器
        :return: WebElement 列表
        """
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    def find_clickable_element(self, locator: tuple):
        """
        查找可点击的元素
        :param locator: 定位器
        :return: WebElement
        """
        return self.wait.until(EC.element_to_be_clickable(locator))
    def find_visible_element(self, locator: tuple):
        """
        查找可见的元素
        :param locator: 定位器
        :return: WebElement
        """
        return self.wait.until(EC.visibility_of_element_located(locator))
    # ==================== 元素操作 ====================
    def click(self, locator: tuple):
        """
        点击元素
        :param locator: 定位器
        """
        self.find_clickable_element(locator).click()
    def input_text(self, locator: tuple, text: str, clear_first: bool = True):
        """
        输入文本
        :param locator: 定位器
        :param text: 要输入的文本
        :param clear_first: 是否先清空输入框
        """
        element = self.find_element(locator)
        if clear_first:
            element.clear()
        element.send_keys(text)
    def input_and_enter(self, locator: tuple, text: str):
        """
        输入文本并回车
        :param locator: 定位器
        :param text: 要输入的文本
        """
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
        element.send_keys(Keys.ENTER)
    def clear_input(self, locator: tuple):
        """
        清空输入框
        :param locator: 定位器
        """
        self.find_element(locator).clear()
    def get_text(self, locator: tuple) -> str:
        """
        获取元素文本
        :param locator: 定位器
        :return: 元素文本内容
        """
        return self.find_element(locator).text
    def get_attribute(self, locator: tuple, attribute: str) -> str:
        """
        获取元素属性值
        :param locator: 定位器
        :param attribute: 属性名
        :return: 属性值
        """
        return self.find_element(locator).get_attribute(attribute)
    def get_value(self, locator: tuple) -> str:
        """
        获取输入框的值
        :param locator: 定位器
        :return: value 属性值
        """
        return self.get_attribute(locator, "value")
    # ==================== 元素状态判断 ====================
    def is_element_present(self, locator: tuple, timeout: int = 5) -> bool:
        """
        判断元素是否存在
        :param locator: 定位器
        :param timeout: 超时时间
        :return: True/False
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except Exception:
            return False
    def is_element_visible(self, locator: tuple, timeout: int = 5) -> bool:
        """
        判断元素是否可见
        :param locator: 定位器
        :param timeout: 超时时间
        :return: True/False
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except Exception:
            return False
    def is_element_clickable(self, locator: tuple, timeout: int = 5) -> bool:
        """
        判断元素是否可点击
        :param locator: 定位器
        :param timeout: 超时时间
        :return: True/False
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            return True
        except Exception:
            return False
    def is_element_selected(self, locator: tuple) -> bool:
        """
        判断元素是否被选中
        :param locator: 定位器
        :return: True/False
        """
        return self.find_element(locator).is_selected()
    # ==================== 下拉框操作 ====================
    def select_by_value(self, locator: tuple, value: str):
        """
        通过 value 选择下拉选项
        :param locator: 定位器
        :param value: 选项的 value 值
        """
        Select(self.find_element(locator)).select_by_value(value)
    def select_by_visible_text(self, locator: tuple, text: str):
        """
        通过可见文本选择下拉选项
        :param locator: 定位器