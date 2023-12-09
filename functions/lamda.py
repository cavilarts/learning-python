from functools import reduce

lambda num : num * 2
multiply = lambda a, b: a * b

print(multiply(2, 4))

numbers = [1, 2, 3]

# map
doubled = map(lambda a: a * 2, numbers)

print(list(doubled))

# filter
filtered = filter(lambda a: a % 2 == 0, numbers)

print(list(filtered))

# reduce

expenses = [
  ("Dinner", 80),
  ("Car repair", 120)
]

total = reduce(lambda a, b: a[1] + b[1], expenses)

print(total)