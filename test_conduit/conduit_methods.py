# Preconditions of TCs' (04-12):
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

username_variable = "C0"
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

    registration_confirm_btn = WebDriverWait(
        browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@class="swal-button swal-button--confirm"]'))
    )
    registration_confirm_btn.click()


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


def create_comment(browser):
    browser.find_element_by_xpath('//button[contains(@class, "accept")]').click()
    testuser3_read_more_link = browser.find_element_by_xpath('//a[@href="#/articles/Laoreet-suspendisse-interdum"]//span[contains(text(),"Read more...")]')
    testuser3_read_more_link.click()

    comment_input = WebDriverWait(
        browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//textarea[@placeholder = "Write a comment..."]'))
    )
    comment_input.send_keys('Test comment.')
    post_comment_btn = browser.find_element_by_xpath('//button[normalize-space()="Post Comment"]')
    post_comment_btn.click()


def username_reset(browser):
    input_your_username = browser.find_element_by_xpath('//input[@placeholder="Your username"]')
    input_your_username.clear()
    input_your_username.send_keys(f"Próba Pista {username_variable}")
    browser.find_element_by_xpath('//button[normalize-space()="Update Settings"]').click()
    update_confirm_btn = WebDriverWait(
        browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//button[normalize-space()="OK"]'))
    )
    update_confirm_btn.click()







