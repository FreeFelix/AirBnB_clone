#!/usr/bin/python3
"""Module creating a User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Handles user-related data"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
