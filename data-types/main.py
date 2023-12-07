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