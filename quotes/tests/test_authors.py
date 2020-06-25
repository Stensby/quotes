import unittest
import base64
import datetime


from ..app import app, db


class TestAuthors(unittest.TestCase):

    def setUp(self):
        credentials = base64.b64encode(b"admin:password").decode('utf-8')
        self.auth_header = {'Authorization': f'Basic {credentials}'}
        db.set_quotes({
            '1': {
                'author': 'Michael',
                'quote': '',
                'created': datetime.datetime.now(),
                'last_updated': datetime.datetime.now()
            },
            '2': {
                'author': 'Michael',
                'quote': '',
                'created': datetime.datetime.now(),
                'last_updated': datetime.datetime.now()
            },
            '3': {
                'author': 'Not Michael',
                'quote': '',
                'created': datetime.datetime.now(),
                'last_updated': datetime.datetime.now()
            }
        })

    def test_authors_list_returns_unique_list(self):
        with app.test_client() as c:
            response = c.get('/authors/', headers=self.auth_header)
            self.assertEqual(response.status_code, 200)
            self.assertCountEqual(response.json, ['Michael', 'Not Michael'])
