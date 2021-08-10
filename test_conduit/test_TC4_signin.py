import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from conduit_registration import *

class TestConduitApp(object):

    def setup(self):
        browser_options = Options()
        browser_options.headless = True
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        self.browser.get("http://localhost:1667/")

    def teardown(self):
        self.browser.quit()

    # TC4 Sign in (precondition: registration of a new user)

    def test_sign_in(self):
        registration_and_login_user(self.browser)

        WebDriverWait(
            self.browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//a[@href="#/login"]'))
        ).click()

        sign_in_email_input = self.browser.find_element_by_xpath('//input[@placeholder="Email"]')
        sign_in_password_input = self.browser.find_element_by_xpath('//input[@placeholder="Password"]')
        sign_in_btn = self.browser.find_element_by_xpath('//button[contains(.,"Sign in")]')

        sign_in_email_input.send_keys("proba_pista_0@proba.com")
        sign_in_password_input.send_keys("Proba123")
        sign_in_btn.click()
        time.sleep(2)

        username_link = self.browser.find_element_by_xpath('//a[@class="nav-link"][normalize-space()="Próba Pista 0"]')
        assert username_link.text == 'Próba Pista 0'
