#!/usr/bin/python3
"""Define Class Review."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review.
    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The review text.
    """

    place_id = ""
    user_id = ""
    text = ""
