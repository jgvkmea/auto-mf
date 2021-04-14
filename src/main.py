import argparse
from selenium import webdriver
from time import sleep

LOGIN_URL = "https://ssnb.x.moneyforward.com/users/sign_in"
ACCOUNT_URL = "https://ssnb.x.moneyforward.com/accounts"

def get_args():
    parser = argparse.ArgumentParser()
    set_args(parser)
    return parser.parse_args()

def set_args(parser):
    parser.add_argument("email", help="MoneyForward Login Email", type=str)
    parser.add_argument("password", help="MoneyForward Login Password", type=str)

def new_driver():
    return webdriver.Chrome("tools/chromedriver")

def login(driver, args):
    driver.find_element_by_id("sign_in_session_service_email").send_keys(args.email)
    driver.find_element_by_id("sign_in_session_service_password").send_keys(args.password)
    driver.find_element_by_id("login-btn-sumit").click()

def update_account_info(driver):
    for i in range(2, len(driver.find_elements_by_css_selector("#account-table > tbody > tr") + 1)):
        btn = driver.find_element_by_css_selector("#account-table > tbody > tr:nth-child({0}) > td:nth-child(5) > form".format(i))
        btn.click()

def main():
    login_args = get_args()
    driver = new_driver()
    
    driver.get(LOGIN_URL)
    login(driver, login_args)
    
    driver.get(ACCOUNT_URL)
    update_account_info(driver)
    
    driver.close()
    driver.quit()

main()
