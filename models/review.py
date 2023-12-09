#!/usr/bin/python3
"""Module defining a Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Manages review objects"""

    place_id = ""
    user_id = ""
    text = ""
