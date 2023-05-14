#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City


all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new User --")
my_user = User()
my_user.first_name = "Betty"
my_user.last_name = "Bar"
my_user.email = "airbnb@mail.com"
my_user.password = "root"
my_user.save()
print(my_user)

print("-- Create a new User 2 --")
my_user2 = User()
my_user2.first_name = "John"
my_user2.email = "airbnb2@mail.com"
my_user2.password = "root"
my_user2.save()
print(my_user2)

print("-- Create a new State 1 --")
my_state = State()
my_state.name = "New York"
my_state.save()
print(my_state)

print("-- Create a new State 2 --")
my_state2 = State()
my_state2.name = "Nevada"
my_state2.save()
print(my_state2)

print("-- Create a new city 1 --")
my_city = City()
my_city.state_id = "hjewiniwiuhw"
my_city.name = "Brooklyn"
my_city.save()
print(my_city)

print("-- Create a new city 2 --")
my_city1 = City()
my_city1.state_id = "wejhwejihwiejwi"
my_city1.name = "Sugarhill"
my_city1.save()
print(my_city1)
