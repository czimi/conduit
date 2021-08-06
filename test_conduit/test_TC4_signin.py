import time
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from conduit_registration import *

class TestConduitApp(object):

    def setup(self):
        browser_options = Options()
        browser_options.headless = False
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        self.browser.get("http://localhost:1667/")

    def teardown(self):
        self.browser.quit()

    # TC4 Sign in (precondition: registration of a new user)

    def test_sign_in(self):
        registration_user(self.browser)
        self.browser.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a').click()
        sign_in_email_input = self.browser.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div/form/fieldset[1]/input')
        sign_in_password_input = self.browser.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div/form/fieldset[2]/input')
        sign_in_btn = self.browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button')

        sign_in_email_input.send_keys("proba_pista_0@proba.com")
        sign_in_password_input.send_keys("Proba123")
        sign_in_btn.click()
        time.sleep(2)

        username_link = self.browser.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[4]/a')
        assert username_link.text == 'Próba Pista 0'