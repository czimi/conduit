import time
import allure
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

# TC1 accept cookies
    @allure.severity(allure.severity_level.NORMAL)
    def test_accept_cookies(self):
        time.sleep(2)
        self.browser.find_element_by_xpath('//button[contains(@class, "accept")]').click()
        time.sleep(2)

        assert self.browser.get_cookies()[0]['value'] == 'accept'