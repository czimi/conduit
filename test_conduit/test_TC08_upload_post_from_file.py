import csv
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

    # TC8 create new blogposts from csv file (precondition: registration of a new user)
    def test_create_new_blogposts_from_file(self):
        conduit_login(self.browser)
        time.sleep(3)

        csv_about_content_list = []

        with open('test_conduit/data_for_auto_upload.csv', 'r', encoding="utf-8") as upload_file:
            csv_reader = csv.reader(upload_file, delimiter=';')
            next(csv_reader)
            for row in csv_reader:
                input_elements = [i.strip(' ') for i in row]
                self.browser.find_element_by_xpath('//a[@href="#/editor"]').click()
                time.sleep(3)
                article_title_input = self.browser.find_element_by_xpath('//input[@placeholder="Article Title"]')
                article_about_input = self.browser.find_element_by_xpath(
                    '//input[contains(@placeholder,"this article about?")]')
                article_text_input = self.browser.find_element_by_xpath(
                    '//textarea[@placeholder="Write your article (in markdown)"]')
                article_tag_input = self.browser.find_element_by_xpath('//input[@placeholder="Enter tags"]')
                time.sleep(3)
                article_title_input.send_keys(input_elements[0])
                article_about_input.send_keys(input_elements[1])
                article_text_input.send_keys(input_elements[2])
                article_tag_input.send_keys(input_elements[3])
                csv_about_content_list.append(input_elements[1])

                self.browser.find_element_by_xpath('//button[contains(.,"Publish Article")]').click()
                time.sleep(3)

                uploaded_articles_about = self.browser.find_elements_by_xpath('//a[@href=f"#/@Próba Pista {username_variable}/"]//parent::div//following-sibling::a/p')
                assert csv_about_content_list == uploaded_articles_about
