from django.test import TestCase, LiveServerTestCase
from django.http import HttpRequest
from selenium.webdriver.common.keys import Keys
import unittest
from selenium import webdriver


class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)


class IndexPageTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def tearDown(self):
        self.browser.quit()

    def testMainPageTitle(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('PyFleet', self.browser.title)


class AccountTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def test_superuser_login(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('PyFleet', self.browser.title)
        self.browser.get('http://127.0.0.1:8000/accounts/login/')
        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        submit = self.browser.find_element_by_id('submit-id-submit')
        username.send_keys('admin')
        password.send_keys('admin')
        submit.click()

    def tearDown(self):
        self.browser.quit()


class OfficeUserTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def tearDown(self):
        self.browser.quit()

    def test_login(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('PyFleet', self.browser.title)
        self.browser.get('http://127.0.0.1:8000/accounts/login/')
        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        submit = self.browser.find_element_by_id('submit-id-submit')
        username.send_keys('Biuro2Basia')
        password.send_keys('VFR$5tgb')
        submit.click()
        self.browser.get('http://127.0.0.1:8000/employee/create')


class BaseViewsTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def tearDown(self):
        self.browser.quit()

    def test_login_and_views(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('PyFleet', self.browser.title)
        self.browser.get('http://127.0.0.1:8000/accounts/login/')
        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        submit = self.browser.find_element_by_id('submit-id-submit')
        username.send_keys('Biuro2Basia')
        password.send_keys('VFR$5tgb')
        submit.click()
        self.browser.get('http://127.0.0.1:8000/employee/list')
        self.assertIn('PyFleet', self.browser.title)
        self.browser.get('http://127.0.0.1:8000/employee/create')
        self.assertIn('PyFleet', self.browser.title)
        self.browser.get('http://127.0.0.1:8000/employee/detail/2')
        self.assertIn('PyFleet', self.browser.title)
        self.browser.get('http://127.0.0.1:8000/customer/list')
        self.assertIn('PyFleet', self.browser.title)
        self.browser.get('http://127.0.0.1:8000/customer/create')
        self.assertIn('PyFleet', self.browser.title)
        self.browser.get('http://127.0.0.1:8000/customer/detail/2')
        self.assertIn('PyFleet', self.browser.title)
        self.browser.get('http://127.0.0.1:8000/order/list')
        self.assertIn('PyFleet', self.browser.title)
        self.browser.get('http://127.0.0.1:8000/order/detail/2')
        self.assertIn('PyFleet', self.browser.title)
        self.browser.get('http://127.0.0.1:8000/order/create')
        self.assertIn('PyFleet', self.browser.title)
        self.browser.get('http://127.0.0.1:8000/truck/list')
        self.assertIn('PyFleet', self.browser.title)
        self.browser.get('http://127.0.0.1:8000/truck/detail/2')
        self.assertIn('PyFleet', self.browser.title)
        self.browser.get('http://127.0.0.1:8000/truck/create')
        self.assertIn('PyFleet', self.browser.title)
        self.browser.get('http://127.0.0.1:8000/daily-routes/list')
        self.assertIn('PyFleet', self.browser.title)
        self.browser.get('http://127.0.0.1:8000/daily-routes/detail/1')
        self.assertIn('PyFleet', self.browser.title)
        self.browser.get('http://127.0.0.1:8000/daily-routes/create')
        self.assertIn('PyFleet', self.browser.title)
        self.browser.get('http://127.0.0.1:8000/dashboard/')
        self.assertIn('PyFleet', self.browser.title)
        self.browser.get('http://127.0.0.1:8000/accounts/profile/')
        self.assertIn('PyFleet', self.browser.title)






# class IndexPageTestDetails(unittest.TestCase):
#
#     def setUp(self):
#         self.browser = webdriver.Firefox()
#         self.addCleanup(self.browser.quit)
#
#     def tearDown(self):
#         self.browser.quit()
#
#     def test_homepage_returns_correct_html(self):
#         response = self.client.get('/')
#         html = response.content.decode('utf8')
#         self.assertTrue(html.startswith('<html>'))

if __name__ == '__main__':
    unittest.main(verbosity=2)