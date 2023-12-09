class Animal:
  def walk(self):
    print("Walking")

# Dog inherit from animal
class Dog(Animal):
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def bark(self):
    print("Woof")

firulais = Dog("Firu", 2)

print(type(firulais))
print(firulais.name)
print(firulais.age)
firulais.bark()
firulais.walk()
