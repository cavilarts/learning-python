def increment(n):
  """Increment number"""
  return n + 1

class Dog:
  """A class representing a doc"""
  def __init__(self, name, age) -> None:
    """Initialize a new dog"""
    self.name = name
    self.age = age
    
  def bark(self):
    """let the dog bark"""
    print("Woof")
    
    
print(help(Dog))