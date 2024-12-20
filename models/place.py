#!/usr/bin/python3
"""Defines class Place."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represent a place.
    Attributes:
        city_id (str): The City id.
        user_id (str): The User id.
        name (str): The name.
        description (str): The description.
        number_rooms (int): The number of rooms.
        number_bathrooms (int): The number of bathrooms.
        max_guest (int): The maximum number of guests.
        price_by_night (int): The price by night.
        latitude (float): The latitude.
        longitude (float): The longitude.
        amenity_ids (list): A list of the Amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
