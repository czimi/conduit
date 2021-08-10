import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from conduit_methods import *

class TestConduitApp(object):

    def setup(self):
        browser_options = Options()
        browser_options.headless = True
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        self.browser.get("http://localhost:1667/")

    def teardown(self):
        self.browser.quit()

    # TC12 Logout (precondition: registration of a new user)

    def test_log_out(self):
        conduit_registration(self.browser)
        logout_element = WebDriverWait(
            self.browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//a[@active-class="active"]'))
        )
        logout_element.click()

        sign_in_link = self.browser.find_element_by_xpath('//a[@href="#/login"]')
        assert sign_in_link.is_enabled(self.browser)
