import datetime
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from conduit_methods import *

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
        conduit_registration(self.browser)
        time.sleep(5)
        editor_element = self.browser.find_element_by_xpath("//a[@href='#/editor']")
        # WebDriverWait(
        #     self.browser, 10).until(
        #     EC.visibility_of_element_located((By.XPATH, "//a[@href='#/editor']"))
        # ).click()

        time.sleep(3)
        article_title_input = self.browser.find_element_by_xpath('//input[@placeholder="Article Title"]')
        article_about_input = self.browser.find_element_by_xpath('//input[contains(@placeholder,"this article about?")]')
        article_text_input = self.browser.find_element_by_xpath('//textarea[@placeholder="Write your article (in markdown)"]')
        article_tag_input = self.browser.find_element_by_xpath('//input[@placeholder="Enter tags"]')

        username_link = self.browser.find_element_by_xpath('//a[contains(@href,"#/@")]')

        article_title_input.send_keys(f'Test Article #{article_number}')
        article_about_input.send_keys(f'Posted by {username_link.text}, {datetime_now}, {article_number}')
        article_text_input.send_keys(
            'Lórum ipse - mint szőkes - ritos nyárgyás szermány, ahol fehérlő bőnyelés, hozás, '
            'fonbázás, celló és más tences gerigy mosít. Egy-egy jobban vagolyozott jontapács '
            'csalmas derhevő tűzdéssel fedizett, hogy minden magára homdást is vike klás, '
            'oldás saját, és máshol nem vagy csak alig ritos tatákat kasolt és émített.')

        article_tag_input.send_keys(f'{username_link.text}, {article_number}')

        time.sleep(3)
        self.browser.find_element_by_xpath('//button[contains(.,"Publish Article")]').click()

        time.sleep(3)
        self.browser.find_element_by_xpath('//a[contains(normalize-space(),"Home")]').click()

        time.sleep(3)
        my_new_article_about = self.browser.find_element_by_xpath(
            f'//p[contains(., "Posted by {username_link.text}, {datetime_now}, {article_number}")]')
        assert my_new_article_about.text == f'Posted by {username_link.text}, {datetime_now}, {article_number}'
