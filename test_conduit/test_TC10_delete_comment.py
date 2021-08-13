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

# TC10 Delete blogpost (precondition: sign in, create comment)

    def test_delete_comment(self):
        conduit_login(self.browser)
        time.sleep(2)
        self.browser.maximize_window()
        time.sleep(2)
        user_name = self.browser.find_element_by_xpath('//a[@class="nav-link"][contains(.,"Próba Pista")]').text
        create_comment(self.browser)

        comment = self.browser.find_element_by_xpath(f'//div[@class="card-footer"][contains(.,"{user_name}")]//parent::div[@class="card"]//p[@class="card-text"]')
        assert comment.text == 'Test comment.'
        delete_comment_btn = self.browser.find_element_by_xpath('//i[@class="ion-trash-a"]')
        delete_comment_btn.click()
        comment_footer = self.browser.find_element_by_xpath(f'//div[@class="card-footer"][contains(.,"{user_name}")]')
        assert comment_footer.is_not_displayed()

