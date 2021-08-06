import time
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class TestConduitApp(object):
    def setup(self):
        browser_options = Options()
        browser_options.headless = True
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        self.browser.get("http://localhost:1667/")

    def teardown(self):
        self.browser.quit()

# TC2 Try to sign up with an inappropriate password

    def test_registration_wrong_pw(self):
        self.browser.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[3]/a').click()
        username_input = self.browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[1]/input')
        email_input = self.browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[2]/input')
        password_input = self.browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[3]/input')
        signup_btn = self.browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button')

        username_input.send_keys("Próba Pista")
        email_input.send_keys("proba_pista_1@proba.com")
        password_input.send_keys("proba1")
        signup_btn.click()
        time.sleep(2)
        allure.attach(self.browser.get_screenshot_as_png(), name="Passwordfailure", attachment_type=AttachmentType.PNG)

        registration_failure_by_pwd_message = self.browser.find_element_by_xpath('/html/body/div[2]/div/div[2]')
        inappropriate_pwd_message = self.browser.find_element_by_xpath('/html/body/div[2]/div/div[3]')

        assert registration_failure_by_pwd_message.text == 'Registration failed!'
        assert inappropriate_pwd_message.text == 'Password must be 8 characters long and include 1 number, 1 uppercase letter, and 1 lowercase letter.'
