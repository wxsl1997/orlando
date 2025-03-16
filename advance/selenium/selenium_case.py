import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

global_driver = None


def chrome_driver():
    options = webdriver.ChromeOptions()
    # 无痕模式
    options.add_argument("--incognito")
    # 禁止脚本
    options.add_argument("--disable-javascript")
    # 禁用图片
    options.add_argument("blink-settings=imagesEnabled=false")
    # 无头模式
    # options.add_argument("--headless")
    # 屏蔽 保存密码 提示
    options.add_experimental_option("prefs", {"credentials_enable_service": False, "profile.password_manager_enabled": False})
    # 屏蔽 浏览器 正受到自动测试软件控制 提示
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    # chrome driver download url: https://googlechromelabs.github.io/chrome-for-testing/
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver


def search_use_bing(keyword):
    global driver

    try:
        # 打开网页
        driver.get('https://cn.bing.com/')
        # wait sb_form_q element presence
        search_form = WebDriverWait(driver, timeout=10).until(
            ec.presence_of_element_located((By.ID, "sb_form_q"))
        )

        # 关键词
        search_form.send_keys(keyword)

        # 回车
        search_form.send_keys(Keys.ENTER)

        # 执行点击查询按钮
        # submit_button = driver.find_element(By.CLASS_NAME, "search")
        # ActionChains(driver).click(submit_button).perform()

        # 执行提交表单
        # submit_button = driver.find_element(By.ID, "sb_form_go")
        # submit_button.submit()
    except Exception as e:
        print(f'failed search use bing, error:{e}')


def search_use_baidu(keyword):
    global driver
    try:
        driver.get('https://www.baidu.com/')
        # wait kw element presence
        search_form = WebDriverWait(driver, timeout=10).until(
            ec.presence_of_element_located((By.ID, "kw"))
        )
        search_form.send_keys(keyword)

    except Exception as e:
        print(f'failed search use baidu, error:{e}')


if __name__ == '__main__':
    global driver
    try:
        driver = chrome_driver()
        search_use_bing('python')
        time.sleep(1)
        search_use_baidu('python')
        time.sleep(1)
    finally:
        driver.quit()
