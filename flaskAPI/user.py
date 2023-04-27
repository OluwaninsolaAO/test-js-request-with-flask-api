#!/usr/bin/env python3
"""User -- simple user class"""

class User:
    """A simple user representation"""

    __users = []

    def __init__(self, name):
        """class constructor"""

        self.name = name
        self.id = self.getCount() + 1
        User.__users.append(self)

    @classmethod
    def getCount(cls):
        """returns a total count of Users obj"""
        return len(cls.__users)

    @classmethod
    def all(cls):
        """returns a list of User objs"""
        return cls.__users

    @classmethod
    def all_dict(cls):
        """returns a list of dictionary reprisentation of users"""
        return [user.__dict__ for user in cls.__users]
