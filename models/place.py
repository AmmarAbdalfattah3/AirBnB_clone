#!/usr/bin/python3
"""Contains the Place model"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place model implementation
    Args:
        city_id (str): City id.
        user_id (str): User id.
        name (str): place name.
        description (str): the place description.
        number_rooms (int): the place room numbers.
        number_bathrooms (int): the place bathroom numbers.
        max_guest (int): the place maximum guest number.
        price_by_night (int): the place night price.
        latitude (float): the place latitude.
        longitude (float): the place logitude.
        amenity_ids (list): Amenity id list.
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
