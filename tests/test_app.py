import unittest
from app import create_app

class ProductTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()
        self.app.testing = True

    def test_add_product(self):
        response = self.app.post('/products', json={"name": "Laptop", "price": 1000})
        self.assertEqual(response.status_code, 201)
        self.assertIn("Laptop", response.get_data(as_text=True))

    def test_get_products(self):
        self.app.post('/products', json={"name": "Phone", "price": 500})
        response = self.app.get('/products')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Phone", response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()

