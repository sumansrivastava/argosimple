import unittest
from app import app

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        # Set up the test client
        self.app = app.test_client()
        self.app.testing = True

    def test_argo_success(self):
        # Send a GET request to the root URL
        result = self.app.get('/')
        
        # Check that the response contains the expected output
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data.decode('utf-8'), 'Hi Suman!!')

if __name__ == '__main__':
    unittest.main()
