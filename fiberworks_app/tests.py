from django.test import TestCase, Client, LiveServerTestCase
from .models import *
from django.urls import reverse  # Import reverse for URL generation
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


import time

class TestModels(TestCase):
    def setUp(self):
        # Set up a Product
        self.product = Product.objects.create(
            name='test product',
            price=999,
            description='test description',
            image='test_image.jpg',
            category='hats',
        )

        # Set up a Homescreen
        self.homescreen = Homescreen.objects.create(
            title='test title',
            paragraph='test paragraph',
        )

    def test_product(self):
        product_url = reverse("product_details", kwargs={"pk": self.product.id})
        product_string = 'test product'

        self.assertEqual(self.product.name, 'test product')
        self.assertEqual(self.product.price, 999)
        self.assertEqual(self.product.description, 'test description')
        self.assertEqual(self.product.image, 'test_image.jpg')
        self.assertEqual(self.product.category, 'hats')
        self.assertEqual(self.product.get_absolute_url(), product_url)
        self.assertEqual(str(self.product), product_string)

    def test_home_str(self):
        homescreen_str = 'test title'
        self.assertEqual(self.homescreen.title, 'test title')
        self.assertEqual(str(self.homescreen), homescreen_str)
        self.assertEqual(self.homescreen.paragraph, 'test paragraph')


class CreateUserTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_create_user(self):
        user_data = {
            'username': 'testuser',
            'password1': 'arstarst',
            'password2': 'arstarst',
        }
        response = self.client.post(reverse('register'), user_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='testuser').exists())

class URLTest(LiveServerTestCase):
    
    def setUp(self):
        # Create a browser instance
        self.browser = webdriver.Chrome()

    def tearDown(self):
        # Close the browser
        self.browser.quit()

    def test_navbar(self):
        # Test that a user can create a new post using a form

        # The user goes to the home page of the blog
        self.browser.get("http://127.0.0.1:8000/")
        time.sleep(2)
        dashboard_link = By.LINK_TEXT, "Dashboard"
        customer_link = By.LINK_TEXT, "Customer view"
        login_link = By.LINK_TEXT, "Login"
        logout_link = By.LINK_TEXT, "Log out"
        register_link = By.LINK_TEXT, "Register"
        home_link = By.LINK_TEXT, "Home"

        try:
            self.browser.find_element(*logout_link).click()
        except:
            print("Already logged out")
        time.sleep(1)
        self.browser.find_element(*login_link).click() 
        time.sleep(1)
        self.browser.find_element(By.ID,'id_username').send_keys('user')
        self.browser.find_element(By.ID,'id_password').send_keys('arstarst')
        self.browser.find_element(By.ID,'submit').click()
        time.sleep(1)
        self.browser.find_element(*home_link).click()
        time.sleep(1)
        self.browser.find_element(*customer_link).click()
        time.sleep(1)
        self.browser.find_element(*dashboard_link).click()



