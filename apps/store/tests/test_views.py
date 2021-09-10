from unittest import skip

from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse
from store.models import Category, Product
from store.views import all_products

# def test_homepage_url(self):
#     '''
#     Test homepage response status
#     '''
#     response = self.Client.get('/')

class TestViewsResponses(TestCase):
    def setUp(self) -> None:
        self.c = Client()
        self.factory = RequestFactory
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, title='django for beginners', 
                    created_by_id=1, slug='django-for-beginners', price='20.00', image='django'
                    )
    
    def test_allowed_hosts(self):
        '''
        Test allowed hosts
        '''
        response = self.c.get('/')
        self.assertEquals(response.status_code, 200)

    def test_product_detail_url(self):
        '''
        Test Product response status
        '''
        response = self.c.get(reverse('store:product_detail', args=['django']))
        self.assertEquals(response.status_code, 200)

    def test_category_list_url(self):
        '''
        Test Category response status
        '''
        response = self.c.get(reverse('store:category_list', args=['django']))
        self.assertEquals(response.status_code, 200)

    def test_home_html(self):
        request = HttpRequest()
        response = all_products(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>Home</title>', html)
        self.assertTrue(html.startwith('\n<!DOCTYPE html>\n'))
        self.assertEquals(response.status_code, 200)

    def test_view_function(self):
        request = self.factory.get('item/django-by-example')
        response = all_products(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>Home</title>', html)
        self.assertTrue(html.startwith('\n<!DOCTYPE html>\n'))
        self.assertEquals(response.status_code, 200)
