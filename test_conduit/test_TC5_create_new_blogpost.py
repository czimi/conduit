import datetime
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from conduit_registration import *

datetime_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
article_number = random.randint(1, 100)


class TestConduitApp(object):

    def setup(self):
        browser_options = Options()
        browser_options.headless = True
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        self.browser.get("http://localhost:1667/")

    def teardown(self):
        self.browser.quit()

    # TC5 create a new blogpost (precondition: registration of a new user)
    def test_create_new_blogpost(self):
        registration_user(self.browser)
        time.sleep(3)
        self.browser.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a').click()
        time.sleep(3)
        article_title_input = self.browser.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[1]/input')
        article_about_input = self.browser.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input')
        article_text_input = self.browser.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[3]/textarea')
        article_tag_input = self.browser.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li/input')

        username_link = self.browser.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[4]/a')

        article_title_input.send_keys(f'Test Article #{article_number}')
        article_about_input.send_keys(f'Posted by {username_link.text}, {datetime_now}, {article_number}')
        article_text_input.send_keys(
            'Lórum ipse - mint szőkes - ritos nyárgyás szermány, ahol fehérlő bőnyelés, hozás, '
            'fonbázás, celló és más tences gerigy mosít. Egy-egy jobban vagolyozott jontapács '
            'csalmas derhevő tűzdéssel fedizett, hogy minden magára homdást is vike klás, '
            'oldás saját, és máshol nem vagy csak alig ritos tatákat kasolt és émített.')

        article_tag_input.send_keys(f'{username_link.text}, {article_number}')

        time.sleep(3)
        self.browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button').click()

        time.sleep(3)
        self.browser.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[1]/a').click()

        time.sleep(3)
        my_new_article_about = self.browser.find_element_by_xpath(
            f'//p[contains(., "Posted by {username_link.text}, {datetime_now}, {article_number}")]')
        assert my_new_article_about.text == f'Posted by {username_link.text}, {datetime_now}, {article_number}'
