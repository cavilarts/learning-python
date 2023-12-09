count = 0

while count < 10:
  print(f"Current count is: {count}")
  count += 1
  
print("After loop")

items = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for index, item in enumerate(items):
  print(item, index)
  
for item in range(15):
  print(f"the item is: {item}")
  
# Interrupt loop

for item in items:
  if item % 2:
    continue
  print(item)