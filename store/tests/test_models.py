from django.test import TestCase
from django.contrib.auth.models import User

from store.models import Category, Product


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.cat1 = Category.objects.create(name='django', slug='django')

    def test_category_model_entry(self):
        """
        Test Category model data insertion  inc types/field attributes
        """
        data = self.cat1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_name_entry(self):
        """
        Test Category model name
        """
        data = self.cat1
        self.assertEqual(str(data.name), 'django')

    def test_category_model_slug_entry(self):
        """
        Test Category model slug
        """
        data = self.cat1
        self.assertEqual(str(data.slug), 'django')


class TestProductsModel(TestCase):
    # In order to test a product we must first create a category to assign it to.

    def setUp(self):
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        self.prod1 = Product.objects.create(
            category_id=1, title='django beginners', slug='django beginners', price='20.00', image='django')

    def test_products_model_entry(self):
        """
        Test Product model data insertion  inc types/field attributes
        """
        data = self.prod1
        self.assertTrue(isinstance(data, Product))

    def test_category_model_name_entry(self):
        """
        Test Category model name
        """
        data = self.prod1
        self.assertEqual(str(data.slug), 'django beginners')
