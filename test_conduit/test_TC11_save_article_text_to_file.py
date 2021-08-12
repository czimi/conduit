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

# TC11 Save content from testuser3's article (precondition: sign in)

    def test_save_article_text(self):
        conduit_login(self.browser)
        time.sleep(2)
        self.browser.find_element_by_xpath('//a[@href="#/@testuser3/"]//parent::div//following-sibling::a/h1').click()
        time.sleep(2)
        article_to_save = self.browser.find_element_by_xpath('//div[@class="row article-content"]//p').text
        allure.attach(self.browser.get_screenshot_as_png(), name="testuser3_article_scrsht", attachment_type=AttachmentType.PNG)
        with open('article_testuser3.txt', 'w', encoding='UTF-8') as text_to_file:
            text_to_file.write(article_to_save)
        with open('article_testuser3.txt', 'r', encoding='UTF-8') as text_to_check:
            saved_article = text_to_check.read()

        assert article_to_save == saved_article

        allure.attach.file('./article_testuser3.txt', attachment_type=allure.attachment_type.TEXT)

        open('article_testuser3.txt', 'w').close()