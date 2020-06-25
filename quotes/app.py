import uuid
import datetime

import bcrypt
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

# Would pull from real DB in prod
USERS = {
    'admin': '$2b$12$Goy2bJJfIwaU5Y1ZtBsMluu9xB66C8ywnsOD5Ucq5j1ZgQWgZQajq'
}

# Would pull from real DB in prod
QUOTES = {
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


@auth.verify_password
def verify_password(username, password):
    if username in USERS and bcrypt.checkpw(password.encode(), USERS.get(username).encode()):
        return username


@app.route('/')
def app_details():
    return 'Python and Flask Quotes App'


@app.route('/quotes/', defaults={'quote_id': None}, methods=['GET', 'POST'])
@app.route('/quotes/<string:quote_id>', methods=['GET', 'PUT', 'POST', 'DELETE'])
@auth.login_required
def quotes(quote_id):
    if request.method == 'GET':
        if quote_id:
            quote = QUOTES.get(quote_id)
            if quote:
                return jsonify({quote_id: quote})
            else:
                return 'Quote not found.', 404
        return jsonify(QUOTES)

    elif request.method == 'POST':
        if quote_id:
            return update_quote(quote_id, request)

        return create_quote(request)

    elif request.method == 'PUT':
        if quote_id:
            return update_quote(quote_id, request)
        else:
            return 'Please use POST to create new quotes', 404

    elif request.method == 'DELETE':
        if quote_id:
            try:
                QUOTES.pop(quote_id)
            except KeyError:
                return f'Failed to delete Quote ID: {quote_id}, invalid ID?', 400
            return f'Quote ID: {quote_id} deleted'


@app.route('/authors')
@auth.login_required
def authors():
    return jsonify(list(set([quote.get('author') for quote in QUOTES])))


def create_quote(request):
    quote = request.json.get('quote')
    author = request.json.get('author')
    if quote and author:
        quote_id = str(uuid.uuid4())
        QUOTES[quote_id] = {'author': author,
                            'quote': quote,
                            'created': datetime.datetime.now(),
                            'last_updated': datetime.datetime.now()}
        return jsonify({quote_id: QUOTES[quote_id]})
    return 'Failed to add new quote, incorrect data format?', 400


def update_quote(quote_id, request):
    quote = request.json.get('quote')
    author = request.json.get('author')
    if quote:
        QUOTES[quote_id]['quote'] = quote
    if author:
        QUOTES[quote_id]['author'] = author
    if quote or author:
        QUOTES[quote_id]['last_updated'] = datetime.datetime.now()
    return jsonify({quote_id: QUOTES[quote_id]})


if __name__ == '__main__':
    app.run('localhost', 5000, debug=True)
