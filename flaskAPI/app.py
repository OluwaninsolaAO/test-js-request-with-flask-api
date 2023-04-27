#!/usr/bin/env python3
"""simple flask API endpoint"""

from flask import Flask, request, jsonify, make_response, abort, url_for
from user import User
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.url_map.strict_slashes = False

users = ['Abraham', 'Isaac', 'Jacob', 'Joseph']
list(map(lambda user: User(user), users))


def get_public_url(user):
    """Includes a public url for Users"""

    resp = {}
    for row in user:
        if row == 'id':
            resp['uri'] = url_for('get_user', id=user['id'], _external=True)
        else:
            resp[row] = user[row]
    return resp


@app.route('/')
def home():
    """index page / root url"""
    return "Hello World!"


@app.route('/users', methods=['GET'])
def get_users():
    """Returns a simple json representation of Users"""
    return jsonify(list(map(get_public_url, User.all_dict())))


@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    """Returns a simple json representation of User"""
    user = [user for user in User.all_dict() if user['id'] == id]
    if len(user) == 0:
        abort(404)
    return jsonify(get_public_url(user[0]))


@app.route('/users', methods=['POST'])
def create_user():
    """Creates a new user and return the json"""
    if not request.json or not 'name' in request.json:
        abort(404)
    user = User(request.json.get('name', 'Nil'))
    return jsonify(user.__dict__), 201


@app.route('/users/repeat', methods=['POST'])
def repeat():
    """Returns a JSON representation recieved back as a response"""

    if not request.json:
        abort(404)
    return jsonify(request.json)


@app.errorhandler(404)
def not_found(error):
    """ Error 404 """
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
