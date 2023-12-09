from enum import Enum


name = "carlos"
print(type(name)) # the type is str

if isinstance(name, str):
  print("Is string")
  
age = 35 # Integer
print(isinstance(age, int))

decimals = 3.14 # Float
print(isinstance(decimals, float))

transform = float(age)
print(isinstance(decimals, float))

ageString = "35"
ageCasted = int(ageString) # casting string to number


is_true = True

class State(Enum):
  ACTIVE = 1
  INACTIVE = 0
  
print(list(State))