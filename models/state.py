#!/usr/bin/python3
"""This is a class User"""

from models.base_model import BaseModel
import datetime


class State(BaseModel):
    """
     create an istance of a state
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        initialize the class
        """
        super().__init__(*args, **kwargs)
        self.updated_at = datetime.datetime.now()
