# 打开QQ邮箱，点击“密码登录”，使用QQ账号密码登录
import getpass
import time

from selenium.webdriver.common.by import By

from utils import DriverTools

ACCOUNT = "1419310155@qq.com"
LOGIN_URL = "https://mail.qq.com/"
MANUAL_WAIT = 300  # 出现验证码/滑块时，留给人工处理的时间（秒）

# 初始化Chrome浏览器驱动
driver = DriverTools.init_chrome()
# 最大化浏览器窗口
DriverTools.maximize_window(driver)
# 打开QQ邮箱登录页
DriverTools.open_url(driver, LOGIN_URL)

# 点击“密码登录”，进入账号密码登录页面
pwd_login_link = DriverTools.find_in_frames(
    driver, (By.XPATH, "//a[contains(normalize-space(.), '密码登录')]"), timeout=20
)
if pwd_login_link is None:
    raise RuntimeError("未找到“密码登录”入口，请确认页面上出现了该链接")
try:
    pwd_login_link.click()
except Exception:
    driver.execute_script("arguments[0].click();", pwd_login_link)

# 填写账号
account_input = DriverTools.find_in_frames(
    driver, (By.CSS_SELECTOR, "input[type='text']"), timeout=20
)
if account_input is None:
    raise RuntimeError("未找到账号输入框")
account_input.clear()
account_input.send_keys(ACCOUNT)

# 填写密码（终端输入，不写进代码）
password_input = DriverTools.find_in_frames(
    driver, (By.CSS_SELECTOR, "input[type='password']"), timeout=20
)
if password_input is None:
    raise RuntimeError("未找到密码输入框")
password = getpass.getpass(f"请输入 {ACCOUNT} 的QQ密码（输入时不显示）：")
password_input.clear()
password_input.send_keys(password)

# 点击登录按钮
login_button = DriverTools.find_in_frames(
    driver,
    (
        By.XPATH,
        "//input[@type='submit'] | //button[contains(normalize-space(.), '登录')] "
        "| //a[contains(normalize-space(.), '登录')]",
    ),
    timeout=10,
)
if login_button is None:
    raise RuntimeError("未找到登录按钮")
try:
    login_button.click()
except Exception:
    driver.execute_script("arguments[0].click();", login_button)

# 等待登录结果：登录页标题包含“登录”，进入邮箱后标题会变化
print("已提交登录，正在等待结果…如出现验证码或滑块，请在浏览器中手动完成，脚本会自动等待")
end_time = time.time() + MANUAL_WAIT
while time.time() < end_time:
    driver.switch_to.default_content()
    if "登录" not in driver.title:
        break
    time.sleep(1)

driver.switch_to.default_content()
if "登录" not in driver.title:
    print(f"登录成功，当前页面标题为：{driver.title}")
else:
    print(f"等待超时，当前页面标题为：{driver.title}，请检查账号密码或验证码是否完成")
