# Precondition of all TCs':
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def registration_and_login_user(browser):
    browser.find_element_by_xpath('//a[normalize-space()="Sign up"]').click()
    username_input = browser.find_element_by_xpath('//input[@placeholder="Username"]')
    email_input = browser.find_element_by_xpath('//input[@placeholder="Email"]')
    password_input = browser.find_element_by_xpath('//input[@placeholder="Password"]')
    signup_btn = browser.find_element_by_xpath('//button[normalize-space()="Sign up"]')

    username_input.send_keys("Próba Pista 0")
    email_input.send_keys("proba_pista_0@proba.com")
    password_input.send_keys("Proba123")
    signup_btn.click()

    element = WebDriverWait(
        browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@class="swal-button swal-button--confirm"]'))
    )
    element.click()

    username_link = browser.find_element_by_xpath('//a[contains(@href,"#/@")]')
    if username_link.is_displayed():
        return
    else:
        # def login_user(browser):
        element = WebDriverWait(
            browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//a[@href="#/login"]'))
        )
        element.click()

        sign_in_email_input = browser.find_element_by_xpath('//input[@placeholder="Email"]')
        sign_in_password_input = browser.find_element_by_xpath('//input[@placeholder="Password"]')
        sign_in_btn = browser.find_element_by_xpath('//button[contains(.,"Sign in")]')

        sign_in_email_input.send_keys("proba_pista_0@proba.com")
        sign_in_password_input.send_keys("Proba123")
        sign_in_btn.click()
