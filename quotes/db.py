import datetime


class Database:

    def __init__(self):
        # Would pull from real DB in prod
        self.users = {
            'admin': '$2b$12$Goy2bJJfIwaU5Y1ZtBsMluu9xB66C8ywnsOD5Ucq5j1ZgQWgZQajq'
        }

        # Would pull from real DB in prod
        self.quotes = {
            '770c57c2-eb1c-4346-a859-471d6ac0a47e': {
                'author': 'Michael Stensby',
                'quote': "Test quotes aren't memorable",
                'created': datetime.datetime.now(),
                'last_updated': datetime.datetime.now()
            },
            '770c57c2-eb1c-4346-a859-471d6ac0a47f': {
                'author': 'Michael Stensby',
                'quote': "Test quotes aren't generally memorable",
                'created': datetime.datetime.now(),
                'last_updated': datetime.datetime.now()
            },
            '770c57c2-eb1c-4346-a859-471d6ac0a47g': {
                'author': 'Not Michael Stensby',
                'quote': 'Test quotes should be memorable!',
                'created': datetime.datetime.now(),
                'last_updated': datetime.datetime.now()
            }
        }

    def get_user(self, username):
        return self.users.get(username)

    def get_users(self):
        return self.users

    def set_users(self, users):
        self.users = users

    def get_quote(self, quote_id):
        return self.quotes.get(quote_id)

    def get_quotes(self):
        return self.quotes

    def set_quotes(self, quotes):
        self.quotes = quotes
