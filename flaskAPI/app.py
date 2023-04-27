#!/usr/bin/env python3
"""simple flask API endpoint"""

from flask import Flask, request, jsonify, make_response, abort
from user import User


app = Flask(__name__)
app.url_map.strict_slashes = False

users = ['Abraham', 'Isaac', 'Jacob', 'Joseph']
list(map(lambda user: User(user), users))


@app.route('/')
def home():
    """index page / root url"""
    return "Hello World!"

@app.route('/users', methods=['GET'])
def get_users():
    """Returns a simple json representation of User"""
    return jsonify(User.all_dict())

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
