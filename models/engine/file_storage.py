#!/usr/bin/python3
"""Building a serialization format using json
and store in file.json"""

import json
import os

class FileStorage:
  """Storage engine.

    Attributes:
        str(__file_path) : The name of the file to save objects to.
        str(__objects): A dictionary of instantiated objects.
    """
  __file_path = "file.json"
  __objects = {}
  
  def all(self):
    return self.__objects
  
  def new(self, obj):
    key = f"{obj.__class__.__name__}.{obj.id}"
    self.__objects[key] = obj
  
  def save(self):
    data = {}
    for key, value in __objects.items():
      data[key] = value.to_dict()
      with open(self.__file_path, mode = "w", encoding="utf-8") as file:
        json.dump(data, file)
  
  def reload(self):
    if os.path.isfile(__file_path):
      with open(self.__file_path, mode = "r", encoding = "utf-8") as file:
        __objects = json.load(file)                     
                           
