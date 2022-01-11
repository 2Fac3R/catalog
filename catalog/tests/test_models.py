"""test_models."""

# Django
from django.test import TestCase

# Catalog
from catalog.models import Product


class ProductModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Set up non-modified objects used by all test methods."""
        Product.objects.create(
            sku='UGG-BB-PUR-1', name='Product 1', price='10.1', brand='Brand 1')

    def test_sku_label(self):
        """Test sku label in model is 'SKU' (uppercase)."""
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('sku').verbose_name
        self.assertEquals(field_label, 'SKU')

    def test_name_label(self):
        """Test name label in model is 'name'."""
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_price_label(self):
        """Test price label in model is 'price'."""
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('price').verbose_name
        self.assertEquals(field_label, 'price')

    def test_brand_label(self):
        """Test brand label in model is 'brand'."""
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('brand').verbose_name
        self.assertEquals(field_label, 'brand')

    def test_sku_max_length(self):
        """Test sku max length is 12."""
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('sku').max_length
        self.assertEquals(max_length, 12)

    def test_name_max_length(self):
        """Test name max length is 100."""
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

    def test_price_max_digits(self):
        """Test price max digits is 5."""
        product = Product.objects.get(id=1)
        max_digits = product._meta.get_field('price').max_digits
        self.assertEquals(max_digits, 5)

    def test_brand_max_length(self):
        """Test brand max length is 100."""
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('brand').max_length
        self.assertEquals(max_length, 100)

    def test_get_absolute_url(self):
        """Test absolute url for catalog-product-detail."""
        product = Product.objects.get(id=1)
        # This will fail if the urlconf is not defined.
        self.assertEquals(product.get_absolute_url(), '/catalog/products/1')
