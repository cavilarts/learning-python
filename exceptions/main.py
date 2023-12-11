
try:
  result = 2 / 0
except ZeroDivisionError:
  print("You cannot divide by zero")
finally:
  result = 1

print(result)

# raise Exception("Hey ya!")

class CatNotFoundException(Exception):
  print("inside")
  pass

try:
  raise CatNotFoundException()
except:
  print("Cat not found :(")