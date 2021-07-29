from django.test import TestCase

from catalog.models import Product
from django.urls import reverse

class ProductListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create products for pagination tests
        number_of_products = 13
        for product_id in range(number_of_products):
            Product.objects.create(
                sku='UGG-BB-PUR-{0}'.format(product_id), 
                name='Product {0}'.format(product_id),
                price='10.{0}'.format(product_id),
                brand='Brand {0}'.format(product_id)
                )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/catalog/products/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/product_list.html')

    def test_pagination_is_ten(self):
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] is True)
        self.assertEqual(len(response.context['product_list']), 10)

    def test_lists_all_products(self):
        # Get second page and confirm it has (exactly) the remaining 3 items
        response = self.client.get(reverse('products')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] is True)
        self.assertEqual(len(response.context['product_list']), 3)