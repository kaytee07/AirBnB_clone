#!/usr/bin/python3
"""this script contains the the base_model class for objects"""


import uuid
import datetime
from . import storage


class BaseModel:
    """defines all common attributes/methods for other classes: """
    def __init__(self, *args, **kwargs):
        self.updated_at = datetime.datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                else:
                    if key == "created_at" or key == "updated_at":
                        value = datetime.datetime.fromisoformat(value)
                        setattr(self, key, value)
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        class_n = self.__class__.__name__
        return f"{class_n} {self.id} {self.__dict__}"

    def save(self):
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        instance_dictionary = self.__dict__
        instance_dictionary['__class__'] = self.__class__.__name__
        instance_dictionary["created_at"] = self.created_at.isoformat()
        instance_dictionary["updated_at"] = self.updated_at.isoformat()
        for key, value in instance_dictionary.items():
            if isinstance(value, (str, int, float, bool)):
                instance_dictionary[key] = value
        return instance_dictionary
