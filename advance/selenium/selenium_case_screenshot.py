import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from selenium_case import chrome_driver

if __name__ == '__main__':
    driver = None
    flag = True
    try:
        driver = chrome_driver()
        driver.get('https://cn.bing.com/')
        # wait sb_form_q element presence
        search_form = WebDriverWait(driver, timeout=10).until(
            ec.presence_of_element_located((By.ID, "sb_form_q"))
        )
        # 元素截图
        search_form.screenshot("/tmp/sb_form_q_screenshot.png")
        # 全屏截图
        driver.save_screenshot('/tmp/sb_form_q_full_screenshot.png')

        time.sleep(3)
    finally:
        driver.quit()
