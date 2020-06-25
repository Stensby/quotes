import datetime
import uuid
import os

import bcrypt
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth

from .db import Database

db = Database()
app = Flask(__name__)
auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    if db.get_user(username) and bcrypt.checkpw(password.encode(), db.get_user(username).encode()):
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
            quote = db.get_quote(quote_id)
            if quote:
                return jsonify({quote_id: quote})
            else:
                return 'Quote not found.', 404
        return jsonify(db.get_quotes())

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
                quotes = db.get_quotes()
                quotes.pop(quote_id)
                db.set_quotes(quotes)
            except KeyError:
                return f'Failed to delete Quote ID: {quote_id}, invalid ID?', 400
            return f'Quote ID: {quote_id} deleted'


@app.route('/authors/')
@auth.login_required
def authors():
    return jsonify(list(set([quote.get('author') for quote in db.get_quotes().values()])))


def create_quote(request):
    quote = request.json.get('quote')
    author = request.json.get('author')
    if quote and author:
        quote_id = str(uuid.uuid4())
        quotes = db.get_quotes()
        quotes[quote_id] = {'author': author,
                            'quote': quote,
                            'created': datetime.datetime.now(),
                            'last_updated': datetime.datetime.now()}
        db.set_quotes(quotes)
        return jsonify({quote_id: quotes[quote_id]})
    return 'Failed to add new quote, incorrect data format?', 400


def update_quote(quote_id, request):
    quote = request.json.get('quote')
    author = request.json.get('author')
    quotes = db.get_quotes()
    if quote:
        quotes[quote_id]['quote'] = quote
    if author:
        quotes[quote_id]['author'] = author
    if quote or author:
        quotes[quote_id]['last_updated'] = datetime.datetime.now()

    db.set_quotes(quotes)
    return jsonify({quote_id: quotes[quote_id]})


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run('0.0.0.0', port=port, debug=True)
