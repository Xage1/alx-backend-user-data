#!/usr/bin/env python3

"""
Hashed password Task
"""

import bcrypt
from user import User
from db import DB
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt
    """
    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password


class Auth:
    """
    Auth class to interact with the authentication database
    """
    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Registers a new User
        """

        try:
            existing_user = self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except ValueError:

            hashed_password = _hash_password(password)

            new_user = self._db.add_user(
                    email=email,
                    hashed_password=hashed_password
            )
            return new_user
    def valid_login(self, email: str, password: str) -> bool:
        try:
            user = self._db.find_user_by(email=email)
            if user is not None:
                pass_bytes = password.encode('utf-8')
                hashed_password = user.hashed_password
                if bcrypt.checkpw(pass_bytes, hashed_password):
                    return True
        except NoResultFound:
            return False
        return False
