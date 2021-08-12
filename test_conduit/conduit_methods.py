# Precondition of all TCs':
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

user_variable_num = random.randint(1, 10000)
# username_variable = f"A{user_variable_num}"
username_variable = f"C0"
email_elotag = f"proba_pista_{username_variable}"


def conduit_registration(browser):
    browser.find_element_by_xpath('//a[normalize-space()="Sign up"]').click()
    username_input = browser.find_element_by_xpath('//input[@placeholder="Username"]')
    email_input = browser.find_element_by_xpath('//input[@placeholder="Email"]')
    password_input = browser.find_element_by_xpath('//input[@placeholder="Password"]')
    signup_btn = browser.find_element_by_xpath('//button[normalize-space()="Sign up"]')

    username_input.send_keys(f"Próba Pista {username_variable}")
    email_input.send_keys(f"{email_elotag}@proba.com")
    password_input.send_keys("Proba123")
    signup_btn.click()

    element = WebDriverWait(
        browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@class="swal-button swal-button--confirm"]'))
    )
    element.click()

    # username_link = browser.find_elements_by_xpath('//a[contains(@href,"#/@")]')


def conduit_login(browser):
    login_element = WebDriverWait(
        browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//a[@href="#/login"]'))
    )
    login_element.click()
    sign_in_email_input = browser.find_element_by_xpath('//input[@placeholder="Email"]')
    sign_in_password_input = browser.find_element_by_xpath('//input[@placeholder="Password"]')
    sign_in_btn = browser.find_element_by_xpath('//button[contains(.,"Sign in")]')

    sign_in_email_input.send_keys(f"{email_elotag}@proba.com")
    sign_in_password_input.send_keys("Proba123")
    sign_in_btn.click()
    time.sleep(2)


def conduit_logout(browser):
    logout_element = browser.find_element_by_xpath("//a[@active-class='active']")
    logout_element.click()
