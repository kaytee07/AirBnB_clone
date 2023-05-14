#!/usr/bin/python3
"""This is a class User"""

from models.base_model import BaseModel
import datetime


class Place(BaseModel):
    """
     create an istance of Place
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

    def __init__(self, *args, **kwargs):
        """
        initialize the class
        """
        super().__init__(*args, **kwargs)
        self.updated_at = datetime.datetime.now()
