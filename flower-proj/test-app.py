# test_app.py
import unittest
from app import app

class FlowerFinderTestCase(unittest.TestCase):
    def setUp(self):
        # Set up the test client
        self.app = app.test_client()
        self.app.testing = True

    def test_index_page_loads(self):
        # Test if the index page loads correctly
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Find Your Flower', response.data)

    def test_result_page_post(self):
        # Test posting data to the result page
        response = self.app.post('/result', data=dict(name='Alice', dob='1990-01-01'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, Alice!', response.data)
        self.assertIn(b'Your flower is:', response.data)

    def test_random_flower_selection(self):
        # Test if a flower is selected randomly
        response = self.app.post('/result', data=dict(name='Bob', dob='1985-05-05'))
        self.assertEqual(response.status_code, 200)
        # Ensure one of the flowers is in the response
        self.assertTrue(any(flower.encode() in response.data for flower in [
            "Rose", "Lily", "Tulip", "Daffodil", "Orchid", 
            "Sunflower", "Daisy", "Lavender", "Marigold", "Jasmine"
        ]))

    def test_invalid_method(self):
        # Test accessing result page with GET method (should fail)
        response = self.app.get('/result')
        self.assertEqual(response.status_code, 405)  # Method Not Allowed

if __name__ == '__main__':
    unittest.main()
