def hello(name = "buddy"):
  print("Hello " + name)
  
hello("Carlos")
hello("Mario")
hello()

def change(value):
  if (type(value) is dict):
    value["name"] = "Mario"
  
val = 1
change(val)
print(val) # 1

my_dict = {"name": "carlos"}
change(my_dict)
print(my_dict)

def say_hi(name):
  if not name:
    return
  print("Hi " + name)
  
say_hi(False)
say_hi("Carlos")

def talk(phrase):
  def say(word):
    print(word)
  
  words = phrase.split(" ")
  
  for word in words:
    say(word)
    
talk("let's have a walk")

def counter():
  count = 0
  
  def increment():
    nonlocal count
    count = count + 1
    return count
    
  return increment

increment = counter()
print(increment()) # 1
print(increment()) # 2
print(increment()) # 3

