import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


LOGIN_URL = "https://ssnb.x.moneyforward.com/users/sign_in"
ACCOUNT_URL = "https://ssnb.x.moneyforward.com/accounts"

headless_chromium = os.getenv('HEADLESS_CHROMIUM', '')
chromedriver = os.getenv('CHROMEDRIVER', '')

def new_driver():
    print(1)
    options = Options()
    print(2)
    options.binary_location = headless_chromium
    print(3)
    options.add_argument('--headless')
    print(4)
    options.add_argument('--no-sandbox')
    print(5)
    options.add_argument('--single-process')
    print(6)
    options.add_argument('--disable-dev-shm-usage')
    print(7)
    options.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36')
    print(8)
    print(chromedriver)
    return webdriver.Chrome(executable_path=chromedriver, options=options)

def login(driver, event):
    driver.find_element_by_id("sign_in_session_service_email").send_keys(event["email"])
    driver.find_element_by_id("sign_in_session_service_password").send_keys(event["password"])
    driver.find_element_by_id("login-btn-sumit").click()

def update_account_info(driver):
    for i in range(2, len(driver.find_elements_by_css_selector("#account-table > tbody > tr")) + 1):
        btn = driver.find_element_by_css_selector("#account-table > tbody > tr:nth-child({0}) > td:nth-child(5) > form".format(i))
        btn.click()

def handler(event, context):
    print('event: {}'.format(event))
    
    driver = new_driver()
    login(driver, event)
    driver.get(ACCOUNT_URL)
    update_account_info(driver)
    
    driver.close()
    driver.quit()
    return "success"
