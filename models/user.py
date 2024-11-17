#!/usr/bin/python3
"""Define class User."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User.
    Attributes:
        email (str): The email.
        password (str): The password.
        first_name (str): The first.
        last_name (str): The last name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
