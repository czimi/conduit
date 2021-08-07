# Precondition of all TC-s:
import time


def registration_user(browser):
    browser.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[3]/a').click()
    username_input = browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[1]/input')
    email_input = browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[2]/input')
    password_input = browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[3]/input')
    signup_btn = browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button')
    username_input.send_keys("Próba Pista 0")
    email_input.send_keys("proba_pista_0@proba.com")
    password_input.send_keys("Proba123")
    signup_btn.click()
    time.sleep(2)
    confirm_btn = browser.find_element_by_xpath('//button[contains(.,"OK")]')
    confirm_btn.click()
