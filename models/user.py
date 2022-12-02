#!/usr/bin/python3
"""A module for the user's model"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class implementaion
    Args:
        email (str): the user email
        password (str): the user password
        first_name (str): the user first name
        last_name (str): the user last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
