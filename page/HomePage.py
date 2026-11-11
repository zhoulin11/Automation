from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    """首页页面对象类"""

    # 页面元素定位器
    LOGO = (By.CSS_SELECTOR, ".logo")
    NAV_BAR = (By.CSS_SELECTOR, ".navbar")
    SEARCH_INPUT = (By.ID, "search-input")
    SEARCH_BUTTON = (By.ID, "search-btn")
    USER_AVATAR = (By.CSS_SELECTOR, ".user-avatar")
    LOGIN_BUTTON = (By.ID, "login-btn")
    REGISTER_BUTTON = (By.ID, "register-btn")
    BANNER = (By.CSS_SELECTOR, ".banner")
    PRODUCT_LIST = (By.CSS_SELECTOR, ".product-list")
    FIRST_PRODUCT = (By.CSS_SELECTOR, ".product-list .product-item:first-child")
    FOOTER = (By.CSS_SELECTOR, "footer")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_home_page(self, url):
        """打开首页"""
        self.driver.get(url)
        self.driver.maximize_window()

    def is_logo_displayed(self):
        """判断logo是否显示"""
        return self.wait.until(EC.visibility_of_element_located(self.LOGO)).is_displayed()

    def is_nav_bar_displayed(self):
        """判断导航栏是否显示"""
        return self.wait.until(EC.visibility_of_element_located(self.NAV_BAR)).is_displayed()

    def input_search_keyword(self, keyword):
        """输入搜索关键词"""
        search_input = self.wait.until(EC.element_to_be_clickable(self.SEARCH_INPUT))
        search_input.clear()
        search_input.send_keys(keyword)

    def click_search_button(self):
        """点击搜索按钮"""
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON)).click()

    def search_product(self, keyword):
        """搜索商品"""
        self.input_search_keyword(keyword)
        self.click_search_button()

    def click_login_button(self):
        """点击登录按钮"""
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

    def click_register_button(self):
        """点击注册按钮"""
        self.wait.until(EC.element_to_be_clickable(self.REGISTER_BUTTON)).click()

    def click_first_product(self):
        """点击第一个商品"""
        self.wait.until(EC.element_to_be_clickable(self.FIRST_PRODUCT)).click()

    def is_user_logged_in(self):
        """判断用户是否已登录"""
        try:
            self.driver.find_element(*self.USER_AVATAR)
            return True
        except:
            return False

    def get_page_title(self):
        """获取页面标题"""
        return self.driver.title

    def get_page_url(self):
        """获取当前页面URL"""
        return self.driver.current_url

    def scroll_to_footer(self):
        """滚动到页面底部"""
        footer = self.wait.until(EC.visibility_of_element_located(self.FOOTER))
        self.driver.execute_script("arguments[0].scrollIntoView();", footer)
