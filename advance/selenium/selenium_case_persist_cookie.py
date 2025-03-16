import json
import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from selenium_case import chrome_driver

if __name__ == '__main__':
    driver = None
    flag = True
    try:
        driver = chrome_driver()
        driver.get("https://passport.bilibili.com/login")
        while flag:
            try:
                # 通过寻找元素判断是否登录
                driver.find_element(By.CLASS_NAME, 'bili-avatar-img')
                flag = False
                print("login success")
            except NoSuchElementException as e:
                time.sleep(3)
                print("unable find avatar image")
        # 存储 cookie
        with open('cookie.json', 'w', encoding='utf-8') as cookie:
            json.dump(driver.get_cookies(), cookie)
    finally:
        driver.quit()
