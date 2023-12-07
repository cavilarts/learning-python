age = 20 # assignation operator

1 + 1 # 2
2 - 1 # 1
2 * 2 # 4
4 / 2 # 2
4 % 3 # 1
4 ** 2 # 16
5 // 2 # 2

print("Mimi" + "is a good cat")

age += 15 # 35

# Comparison

a = 1
b = 2

a == b # False
a != b # True
a > b # False
a <= b # true

condition1 = True
condition2 = False

not condition1 # False
condition1 and condition2 # false
condition1 or condition2 # True

print(0 or 1) # 1
print(False or "hey") # 'hey'
print("hi" or "hey") # 'hi'
print([] or False) # False
print(False or []) # []


print(0 and 1) # 0
print(1 and 0) # 0
print(False and "hey") # False
print("hi" and "hey") # 'hey'
print([] and False) # []
print(False and []) # False

# Binary operators
# & performs binary AND
# | performs binary OR
# ^ performs binary XOR
# ~ performs binary NOT
# << shift left operator
# >> shift right operator

# Ternary operator
is_adult = True if age > 18 else False