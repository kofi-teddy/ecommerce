from django.contrib.auth.models import User
from django.test import TestCase
from store.models import Category, Product


class TestCategoriesModel(TestCase):

    def setup(self):
        self.data1 = Category.objects.create(name='django', slug='django')

    def test_category_model_entry(self):
        '''
        Test Category Model data insertion/types/fieds attributes 
        '''
        data = self.data1
        self.assertTrue(isinstance(data, Category))
    
    def test_category_model_entry(self):
        '''
        Test Category model return name
        '''
        data = self.data1
        self.assertEquals(str(data), 'django')


class TestProductModel(TestCase):
    def setup(self):
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, title='django for beginners', 
                    created_by_id=1, slug='django-for-beginners', price='20.00', image='django'
                    )

    def test_product_models_entry(self):
        '''
        Test Product model data insertion/types/field attribute 
        '''
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEquals(str(data), 'django for beginners')
