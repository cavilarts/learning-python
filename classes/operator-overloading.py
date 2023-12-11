class Dog:
  # the Dog Class
  def __init__(self, name, age) -> None:
    self.name = name
    self.age = age
    
  def __gt__(self, other):
    return True if self.age > other.age else False
    
firu = Dog('Firulais', 4)
cani = Dog('Caniche', 2)

print(firu > cani)