# Precondition of all TCs':
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

username_variable = "0D"
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

def conduit_logout(browser):
    browser.find_element_by_xpath('//a[@active-class="active"]').click()

    # username_link = browser.find_elements_by_xpath('//a[contains(@href,"#/@")]')
    # # if username_link.is_displayed():
    # #     return None
    # if len(username_link) == 0:
    #     element = WebDriverWait(
    #         browser, 10).until(
    #         EC.visibility_of_element_located((By.XPATH, '//a[@href="#/login"]'))
    #     )
    #     element.click()
    #
    #     sign_in_email_input = browser.find_element_by_xpath('//input[@placeholder="Email"]')
    #     sign_in_password_input = browser.find_element_by_xpath('//input[@placeholder="Password"]')
    #     sign_in_btn = browser.find_element_by_xpath('//button[contains(.,"Sign in")]')
    #
    #     sign_in_email_input.send_keys("proba_pista_0Y@proba.com")
    #     sign_in_password_input.send_keys("Proba123")
    #     sign_in_btn.click()

