import time
import allure
from allure_commons.types import AttachmentType
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

# TC09 Modify blogpost content (precondition: sign in)
    def modify_blogpost_content(self):
        conduit_login(self.browser)
        create_blogpost_for_testing(self.browser)
        time.sleep(3)
        self.browser.find_element_by_xpath('//a[contains(normalize-space(),"Home")]').click()
        time.sleep(2)
        self.browser.find_element_by_xpath(f'//h1[contains(.,"test_blogpost_{datetime_now}")]').click()
        time.sleep(2)
        self.browser.find_element_by_xpath('//a[contains(.,"Edit Article")]').click()
        time.sleep(2)
        blogpost_text_input = self.browser.find_element_by_xpath('//textarea[@placeholder="Write your article (in markdown)"]')
        blogpost_text_input.clear()
        blogpost_text_input.send_keys('A kasárában egy eléggé piszalmarsodt, önözös tratokra nem hegyezdő, fürk várkódt ki. Valaki azért, mert neki nem lesztett meg a hált srót és gyorica, mások pedig saját párdáruk bosztatását kélkedik be.')
        self.browser.find_element_by_xpath('//button[normalize-space()="Publish Article"]').click()

