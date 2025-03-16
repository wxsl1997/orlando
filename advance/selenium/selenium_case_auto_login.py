import json
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from selenium_case import chrome_driver


def new_cookies(cookies):
    current_domain = {}  # 域 cookie 映射
    for cookie in cookies:
        domain = cookie['domain']
        if domain in current_domain:
            current_domain[domain].append(cookie)
        else:
            current_domain[domain] = []
    max_cnt = 0
    ans_domain = ''
    for domain in current_domain.keys():
        cnt = len(current_domain[domain])
        if cnt > max_cnt:
            max_cnt = cnt
            ans_domain = domain
    return current_domain[ans_domain]


if __name__ == '__main__':
    driver = None
    try:
        driver = chrome_driver()
        # 读取 cookie
        with open('cookie.json', 'r', encoding='utf-8') as txt:
            driver.get("https://www.bilibili.com/")

            print("start load cookie")
            cookies = json.load(txt)
            for cookie in new_cookies(cookies):
                driver.add_cookie(cookie)
            print("finished load cookie")

            # refresh page
            driver.refresh()

            # wait avatar appear
            WebDriverWait(driver, timeout=10).until(
                ec.presence_of_element_located((By.CLASS_NAME, "bili-avatar-img"))
            )

            # sleep few second
            time.sleep(3)
    finally:
        driver.quit()
