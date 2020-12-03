from django.test import TestCase, LiveServerTestCase, RequestFactory
from django.http import HttpRequest
from selenium.webdriver.common.keys import Keys
import unittest
from selenium import webdriver

###
# Please ensure Firefox is installed geckodriver is in PATH before running tests
# Ensure user / password variables are updated in accordance with current DB entries
###

# users setup
from core.models import Customer

admin_username = 'admin'
admin_pass = 'admin'

office_username = 'Biuro2Basia'
office_pass = 'VFR$5tgb'


class CustomerModelTest(TestCase):
    def setUp(self):
        Customer.objects.create(company_name='Test Company Name', NIP='0000000111100')

    def test_read(self):
        self.assertTrue(Customer.objects.filter(NIP='0000000111100').exists())
        self.assertTrue(Customer.objects.filter(company_name='Test Company Name').exists())


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
        username.send_keys(admin_username)
        password.send_keys(admin_pass)
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
        username.send_keys(office_username)
        password.send_keys(office_pass)
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
        username.send_keys(office_username)
        password.send_keys(office_pass)
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


class PostingToDBTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def tearDown(self):
        self.browser.quit()

    def test_customer_creation(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('PyFleet', self.browser.title)
        self.browser.get('http://127.0.0.1:8000/accounts/login/')
        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        submit = self.browser.find_element_by_id('submit-id-submit')
        username.send_keys(office_username)
        password.send_keys(office_pass)
        submit.click()
        self.browser.get('http://127.0.0.1:8000/customer/create')
        self.assertIn('PyFleet', self.browser.title)
        company_name = self.browser.find_element_by_id('id_company_name')
        nip = self.browser.find_element_by_id('id_NIP')
        submit_2 = self.browser.find_element_by_id('submit-id-submit')
        company_name.send_keys('Test Company Name')
        nip.send_keys('0000000111100')
        submit_2.click()
        self.browser.get('http://127.0.0.1:8000/customer/list')



        # customer_items = self.customer.exists()
        # self.assertTrue(customer_items, msg='Customer objects exist')
        # test_customer = self.customer.filter(company_name='Test Company Name').exists()
        # self.assertTrue(test_customer, msg='Test Customer object exist')
        # self.assertTrue(Customer.objects.filter(NIP='0000000111100').exists())




if __name__ == '__main__':
    unittest.main(verbosity=2)
