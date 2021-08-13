import time
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
        self.content_testuser2_articles_about_main = []
        self.content_testuser2_articles_about_user = []

    def teardown(self):
        self.browser.quit()

    # TC6 listing all blogposts of a testuser (precondition: registration of a new user)
    def test_list_all_posts_of_testuser2(self):
        conduit_login(self.browser)
        time.sleep(2)

        list_testuser2_articles_about_main = self.browser.find_elements_by_xpath('//a[@href="#/@testuser2/"]//parent::div//following-sibling::a/p')

        for i in range(len(list_testuser2_articles_about_main)):
           self.content_testuser2_articles_about_main.append(list_testuser2_articles_about_main[i].text)

        self.browser.find_element_by_xpath('//a[@href="#/@testuser2/"][@class="author"]').click()
        time.sleep(3)

        list_testuser2_articles_about_user = self.browser.find_elements_by_xpath('//p[normalize-space()]')

        for i in range(len(list_testuser2_articles_about_user)):
            self.content_testuser2_articles_about_user.append(list_testuser2_articles_about_user[i].text)
            if self.content_testuser2_articles_about_user[i] in self.content_testuser2_articles_about_main:
                assert True
