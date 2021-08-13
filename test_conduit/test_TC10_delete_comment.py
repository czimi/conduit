import time
import allure
from allure_commons.types import AttachmentType
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

# TC10 Delete blogpost (precondition: sign in, create comment)

    def test_delete_comment(self):
        conduit_login(self.browser)
        time.sleep(4)
        user_name = self.browser.find_element_by_xpath('//a[@class="nav-link"][contains(.,"Próba Pista")]').text
        create_comment(self.browser)
        time.sleep(2)
        allure.attach(self.browser.get_screenshot_as_png(), name="Created_comment", attachment_type=AttachmentType.PNG)

        comment = self.browser.find_element_by_xpath(f'//div[@class="card-footer"][contains(.,"{user_name}")]//parent::div[@class="card"]//p[@class="card-text"]')
        assert comment.text == 'Test comment.'
        delete_comment_btn = self.browser.find_element_by_xpath('//i[@class="ion-trash-a"]')
        delete_comment_btn.click()
        time.sleep(2)
        comment_block = self.browser.find_elements_by_xpath('//div[@class="card-block"]/p')
        assert len(comment_block) == 0

