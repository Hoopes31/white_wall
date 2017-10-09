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

        # User sees login as the root page
        self.assertIn('Login', self.browser.title)

        # User can navigate to 'sign up'
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

    def test_login_success(self):
        self.browser.get('http://localhost:8000')
        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        submit = self.browser.find_element_by_xpath('//input[@type="submit"]')

        username.send_keys('admin')
        password.send_keys('testing123')
        submit.click()

        self.assertIn('Splash Welcome', self.browser.title)

    def sign_up_root_loads_properly(self):
        self.browser.get('http://localhost:8000/sign_up')

        # User sees sign up page
        self.assertIn('Sign Up!', self.browser.title)

        # User can navigate to 'login'
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

        # User can user the in app browser to navigate the internet
        
        # User can select annotations and read their contents

        # User can upload answers to annotations

        # User can click answer links

        # User can view article summary

if __name__ == '__main__':
    unittest.main()