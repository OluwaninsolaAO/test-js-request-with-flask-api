#!/usr/bin/env python3
"""simple flask API endpoint"""

from flask import Flask, request
from user import User


app = Flask(__name__)
app.url_map.strict_slashes = False

users = ['Abraham', 'Isaac', 'Jacob', 'Joseph']
all_users_dict = [User(user).__dict__ for user in users]

@app.route('/users', methods=['GET', 'PUT'])
def users():
    """Returns a simple json representation of User"""
    import json

    if request.method == 'GET':
        return json.dumps(all_users_dict)
    elif request.method == 'PUT':
        return "Recieved"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
