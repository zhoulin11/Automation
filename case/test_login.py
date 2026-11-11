"""用例：QQ邮箱账号密码登录"""
import getpass
import os
import sys
import time

from selenium import webdriver

# 保证以脚本方式运行时能导入项目根目录下的 base、page 包
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from page.LoginPage import LoginPage

ACCOUNT = os.environ.get("QQ_ACCOUNT", "1419310155")


def get_password():
    """优先读取环境变量 QQ_PASSWORD，未设置时在终端输入（输入时不显示）"""
    return os.environ.get("QQ_PASSWORD") or getpass.getpass(
        f"请输入 {ACCOUNT} 的QQ密码（输入时不显示）："
    )


def test_login():
    """打开QQ邮箱，使用账号密码登录并校验登录结果"""
    password = get_password()
    driver = webdriver.Chrome()
    try:
        login_page = LoginPage(driver)
        login_page.maximize_window()
        login_page.login(ACCOUNT, password)

        print("已提交登录，如出现验证码或滑块请手动完成，脚本会自动等待")
        assert login_page.wait_login_success(timeout=300), "登录失败：请检查账号密码或验证码是否完成"
        print(f"登录成功，当前页面标题：{login_page.get_title()}")
        time.sleep(5)
    finally:
        driver.quit()


if __name__ == "__main__":
    test_login()
