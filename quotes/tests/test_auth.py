import unittest
import base64


from ..quotes import app


class TestBasicAuth(unittest.TestCase):
    def test_no_auth_provided_should_return_401(self):
        with app.test_client() as c:
            response = c.get('/quotes/')
            self.assertEqual(response.status_code, 401)

    def test_invalid_auth_provided_should_return_401(self):
        credentials = base64.b64encode(b'admin:wrong_password').decode('utf-8')
        with app.test_client() as c:
            response = c.get('/quotes/', headers={'Authorization': f'Basic {credentials}'})
            self.assertEqual(response.status_code, 401)

    def test_valid_auth_provided_should_return_200(self):
        credentials = base64.b64encode(b'admin:password').decode('utf-8')
        with app.test_client() as c:
            response = c.get('/quotes/', headers={'Authorization': f'Basic {credentials}'})
            self.assertEqual(response.status_code, 200)
