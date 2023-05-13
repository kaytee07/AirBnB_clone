#!/usr/bin/python3
"""Base Model Class for all attributes and methods for other classes
"""

import uuid
import datetime
from __init__ import storage

class BaseModel:
  """defines all common attributes/methods for other classes: """
  
  def __init__(self, *args, **kwargs):
    """this method is to initiali """
    #self.id = str(uuid.uuid4())
    #self.created_at = datetime.datetime.now()
    self.updated_at = datetime.datetime.now()
    
    if len(kwargs) != 0:
      for key, value in kwargs.items():
        if key == "created_at" || key =="updated_at"
        self.key = datetime.datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
        elif key == "__class__":
          continue
        else:
          self.key = value
      else:
        storage.new()
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        
  def __str__(self):
    class_n=self.__class__.__name___
    return f"class_n {self.id} {self.__dict__} "
  
  def save(self):
    storage.save()
    self.updated_at = datetime.now()

  def to_dict(self): 
    instance_dictionary=self.__dict__
    instance_dictionary['__class__']=self.__class__.__name__
    self.created_at = isoformat(self.created_at)
    self.updated_at = isoformat(self.updated_at)
    for key, value in instance_dictionary.items():
      if isinstance(value, (str, int, float, bool)):
        instance_dictionary[key]=value
    
    return instance_dictionary

