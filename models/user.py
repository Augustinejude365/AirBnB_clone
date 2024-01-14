#!/usr/bin/python3
"""This line of codes defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """
    The User's representation.
    Attributes:
    email (str): The email of the user.
    password (str): The password of the user.
    first_name (str): The first name of the user.
    last_name (str): The last name of the user.
    """

    emaill = ""
    password = ""
    first_name = ""
    last_name = ""
