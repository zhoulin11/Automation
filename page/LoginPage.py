"""QQ邮箱登录页页面对象"""
from selenium.webdriver.common.by import By

from base.BasePage import BasePage


class LoginPage(BasePage):
    """QQ邮箱登录页，登录表单位于页面 iframe 内"""

    URL = "https://mail.qq.com/"

    # 页面元素定位器
    PASSWORD_LOGIN_LINK = (By.ID, "switcher_plogin")
    ACCOUNT_INPUT = (By.ID, "u")
    PASSWORD_INPUT = (By.ID, "p")
    LOGIN_BUTTON = (By.ID, "login_button")

    def open(self):
        """打开QQ邮箱首页"""
        self.open_url(self.URL)

    def switch_to_password_login(self):
        """切换为账号密码登录方式"""
        self.click_element(self.find_in_frames(self.PASSWORD_LOGIN_LINK, timeout=20))

    def input_account(self, account):
        """输入账号"""
        self.input_element(self.find_in_frames(self.ACCOUNT_INPUT), account)

    def input_password(self, password):
        """输入密码"""
        self.input_element(self.find_in_frames(self.PASSWORD_INPUT), password)

    def click_login(self):
        """点击登录按钮"""
        self.click_element(self.find_in_frames(self.LOGIN_BUTTON))

    def login(self, account, password):
        """执行完整登录流程"""
        self.open()
        self.switch_to_password_login()
        self.input_account(account)
        self.input_password(password)
        self.click_login()

    def wait_login_success(self, timeout=300):
        """等待进入邮箱，登录页标题包含“登录”，登录成功后标题会变化"""
        return self.wait_title_not_contains("登录", timeout)
