from selenium import webdriver
import logging
import unittest

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)
browser = webdriver.Chrome()

class SiteIsUp(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        logging.info('%s COMPLETE', self)
        browser.quit()

    def test_root_page_loads_properly(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Login', self.browser.title)

        sign_up = self.browser.find_element_by_link_text('Sign Up!')
        self.assertIsNotNone(sign_up)
        sign_up.click()

    def test_login_fails(self):
        self.browser.get('http://localhost:8000')
        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        submit = self.browser.find_element_by_xpath('//input[@type="submit"]')

        username.send_keys('wrong_user')
        password.send_keys('wrong_password')
        submit.click()

        invalid = self.browser.find_element_by_class_name('error')
        self.assertIsNotNone(invalid)

    def sign_up_root_loads_properly(self):
        self.browser.get('http://localhost:8000/sign_up')
        self.assertIn('Sign Up!', self.browser.title)

        login = self.browser.find_element_by_link_text('Login')
        self.assertIsNotNone(login)
        login.click()

    def test_sign_up_fails_exisiting_user_email(self):
        self.browser.get('http://localhost:8000/sign_up')
        username = self.browser.find_element_by_id('id_username')
        first_name = self.browser.find_element_by_id('id_first_name')
        last_name = self.browser.find_element_by_id('id_last_name')
        email = self.browser.find_element_by_id('id_email')
        password = self.browser.find_element_by_id('id_password')
        confirm_password = self.browser.find_element_by_id('id_confirm_password')
        submit = self.browser.find_element_by_xpath('//input[@type="submit"]')

        username.send_keys('fresh_user')
        first_name.send_keys('Bob')
        last_name.send_keys('Dole')
        email.send_keys('admin@admin.com')
        password.send_keys('testing123')
        confirm_password.send_keys('testing123')
        submit.click()

        error = self.browser.find_element_by_class_name('errorlist')
        self.assertIsNotNone(error)

    def test_login_success_welcome(self):
        self.browser.get('http://localhost:8000')
        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        submit = self.browser.find_element_by_xpath('//input[@type="submit"]')

        username.send_keys('admin')
        password.send_keys('testing123')
        submit.click()

        self.assertIn('Splash Welcome', self.browser.title)
        logout = self.browser.find_element_by_xpath('//a[@href="/logout"]')
        logout.click()

    def test_login_white_wall(self):
        self.browser.get('http://localhost:8000')
        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        submit = self.browser.find_element_by_xpath('//input[@type="submit"]')

        username.send_keys('admin')
        password.send_keys('testing123')
        submit.click()

        selectArticle = self.browser.find_element_by_xpath('//input[@type="submit"]')
        selectArticle.click()

        # User can use the in app browser to navigate the docs
        white_wall_browser = self.browser.find_element_by_id('iframe')
        url = white_wall_browser.get_attribute('src')
        self.assertIsNotNone(white_wall_browser)
        self.assertIn('www.django', url)

        # User can upload new annotations
        add_annotation = self.browser.find_element_by_xpath('//input[@value="Annotate!"]')
        self.assertIsNotNone(add_annotation)
        
        # User can add answers to annotations
        add_comment = self.browser.find_element_by_xpath('//input[@value="Comment!"]')
        self.assertIsNotNone(add_comment)

        # User can select a different article to browse
        change_article = self.browser.find_element_by_xpath('//input[@value="Choose Article"]')
        change_article.click()

        # User can search articles by custom google search
        submit_search = self.browser.find_element_by_xpath('//input[@type="image"]')
        google_search = self.browser.find_element_by_id('gsc-i-id1')
        google_search.send_keys('Django: Build in User model')
        submit_search.click()

        # User can view article summary
        summary = self.browser.find_element_by_id('annotation_summary')
        self.assertIsNotNone(summary)

if __name__ == '__main__':
    unittest.main()