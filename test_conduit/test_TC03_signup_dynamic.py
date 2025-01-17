import random
import bcrypt
import time
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestConduitApp(object):

    def setup(self):
        browser_options = Options()
        browser_options.headless = True
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        self.browser.get("http://localhost:1667/")
        self.user_variable = random.randint(1, 10000)

    def teardown(self):
        self.browser.quit()

    # TC3 Sign up with an appropriate password and "dynamic" user data

    def test_registration_dynamic_userdata(self):
        self.browser.find_element_by_xpath('//a[normalize-space()="Sign up"]').click()
        username_input = self.browser.find_element_by_xpath('//input[@placeholder="Username"]')
        email_input = self.browser.find_element_by_xpath('//input[@placeholder="Email"]')
        password_input = self.browser.find_element_by_xpath('//input[@placeholder="Password"]')
        signup_btn = self.browser.find_element_by_xpath('//button[normalize-space()="Sign up"]')

        username_input.send_keys(f"Próba Pista {self.user_variable}")
        email_input.send_keys(f"proba_pista_{self.user_variable}@proba.com")
        password_input.send_keys("Proba123")
        signup_btn.click()
        time.sleep(3)
        registration_successful_message = self.browser.find_element_by_xpath('//div[@class="swal-text"]')
        assert registration_successful_message.text == "Your registration was successful!"

        WebDriverWait(
            self.browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@class="swal-button swal-button--confirm"]'))
        ).click()

        username_link = self.browser.find_element_by_xpath(
            f'//a[@class="nav-link"][normalize-space()="Próba Pista {self.user_variable}"]')
        assert username_link.text == f'Próba Pista {self.user_variable}'

    def test_attach_userdata(self):
        passwd = b'Proba123'
        salt = bcrypt.gensalt()
        hashed_passwd = bcrypt.hashpw(passwd, salt)
        allure.attach(
            f"username: Próba Pista {self.user_variable},\nemail: proba_pista_{self.user_variable}@proba.com,\nPassword: {hashed_passwd}",
            attachment_type=allure.attachment_type.TEXT)
