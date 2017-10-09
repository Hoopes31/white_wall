from selenium import webdriver
import unittest

browser = webdriver.Chrome()


class SiteIsUp(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        browser.quit()

    def test_site_is_running(self):
        # User visits awesome new annotations website's home page
        browser.get('http://localhost:8000')

        # User sees the site name 'White Wall' in the title of the running application
        self.assertIn('Api', self.browser.title)
        self.fail('Finish the test!')

        # User sees login as the root page

        # User can navigate to 'sign up'

        # User can Login and are taken to the in app control window

        # User can user the in app browser to navigate the interenet

        # User can select annotations and read their contents

        # User can upload answers to annotations

        # User can click answer links

        # User can view article summary

if __name__ == '__main__':
    unittest.main()