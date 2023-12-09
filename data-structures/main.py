items = ["Bag", "Phone", "Toy", "map"] # this is a list

# In both cases bellow we modified the original list
# items.sort() # ['Bag', 'Phone', 'Toy', 'map'] Note that lowercase were not sorted
# items.sort(key=str.lower) Now it is being sorted

# In this case it is not modified
print(sorted(items, key=str.lower))
print(items)


# Tuples

names = ("Roger", "Syd")

print(names[0])
print(names.index("Roger"))
print(len(names))
print("Roger" in names)

# Dictionaries

dog = { "name": "Roger", "age": 8, "color": "black" }

dog["favorite_food"] = "Bones"

del dog["color"]

dog_copy = dog.copy()

print(dog["name"])
print(dog.get("name"))
print(dog.popitem())

# Sets

names_set = {"Roger", "Syd"}
names_set2 = {"Roger"}
intersect = names_set & names_set2
print(intersect) # Roger

names_set3 = {"Mario"}
union = names_set | names_set3
print(union) # Syd, Roger, Mario

difference =  names_set - names_set2
print(difference) # Syd