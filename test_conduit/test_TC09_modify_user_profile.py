
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conduit_methods import *

class TestConduitApp(object):

    def setup(self):
        browser_options = Options()
        browser_options.headless = True
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        self.browser.get("http://localhost:1667/")

    def teardown(self):
        self.browser.quit()

# TC09 Modify user_profile (precondition: sign in)
    def test_modify_user_name(self):
        conduit_login(self.browser)
        time.sleep(3)
        self.browser.find_element_by_xpath('//a[@href="#/settings"]').click()
        time.sleep(2)
        input_your_username = self.browser.find_element_by_xpath('//input[@placeholder="Your username"]')
        input_your_username.clear()
        input_your_username.send_keys(f"Próba Pista {username_variable}C")
        self.browser.find_element_by_xpath('//button[normalize-space()="Update Settings"]').click()
        update_confirm_btn = WebDriverWait(
            self.browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//button[normalize-space()="OK"]'))
        )
        update_confirm_btn.click()
        new_username_link = self.browser.find_element_by_xpath(f'//a[@class="nav-link"][contains(.,"Próba Pista {username_variable}C")]')
        assert new_username_link.is_displayed()
        username_reset(self.browser)

