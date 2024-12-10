from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status
from products.models import Product, Category


class ProductTestCase(APITestCase):
    
    def setUp(self):
        self.category1 = Category.objects.create(title="Electronics")
        self.category2 = Category.objects.create(title="Clothing")
        self.user = User.objects.create_user(
            username='testuser', 
            password='this_is_a_test',
            email='testuser@test.com'
        )
        self.product1 = Product.objects.create(
            title="Laptop", description="Gaming Laptop", price=1500.00, stock=10, category=self.category1, seller=self.user
        )
        self.product2 = Product.objects.create(
            title="T-shirt", description="Cotton T-shirt", price=20.00, stock=50, category=self.category2, seller=self.user
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
    
    def test_get_all_categories(self):
        response = self.client.get('/api/products/categories/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_one_category(self):
        response = self.client.get(f'/api/products/categories/{self.category1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.category1.title)

    def test_create_category(self):
        data = {'title': 'Furniture'}
        response = self.client.post('/api/products/categories/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Furniture')

    def test_update_category(self):
        data = {'title': 'Updated Electronics'}
        response = self.client.put(f'/api/products/categories/{self.category1.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Electronics')

    def test_delete_category(self):
        response = self.client.delete(f'/api/products/categories/{self.category2.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get('/api/products/categories/')
        self.assertEqual(len(response.data), 1) 

    def test_get_all_products(self):
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_product(self):
        data = {
            'title': 'Smartwatch',
            'description': 'Fitness smartwatch',
            'price': 200.00,
            'stock': 10,
            'category': self.category1.id,
        }
        response = self.client.post('/api/products/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_one_product(self):
        response = self.client.get(f'/api/products/{self.product1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.product1.title)
        self.assertEqual(response.data['category'], self.product1.category.title)

    def test_update_product(self):
        data = {
            'title': 'Updated Laptop',
            'description': 'Updated gaming laptop',
            'price': 1800.00,
            'stock': 5,
            'category': self.category1.id,
        }
        response = self.client.put(f'/api/products/{self.product1.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Laptop')

    def test_delete_product(self):
        response = self.client.delete(f'/api/products/{self.product2.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get('/api/products/')
        self.assertEqual(len(response.data), 1)

    def test_create_product_with_invalid_category(self):
        invalid_category_id = 9999
        data = {
            'title': 'Smartwatch',
            'description': 'Fitness smartwatch',
            'price': 200.00,
            'stock': 10,
            'category': invalid_category_id,
        }
        response = self.client.post('/api/products/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)