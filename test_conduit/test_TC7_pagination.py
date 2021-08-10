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

    # TC7 Pagination on Conduit (precondition: registration of a new user)
    def test_pagination(self):
        conduit_registration(self.browser)
        time.sleep(2)
        page_1 = self.browser.find_element_by_xpath('//li[@data-test="page-link-1"]')
        assert page_1.get_attribute("class") == "page-item active"

        page_2 = self.browser.find_element_by_xpath('//li[@data-test="page-link-2"]')
        assert page_2.get_attribute("class") == "page-item"

        self.browser.find_element_by_xpath('//a[@class="page-link"][normalize-space()="2"]').click()
        assert page_1.get_attribute("class") == "page-item"
        assert page_2.get_attribute("class") == "page-item active"
