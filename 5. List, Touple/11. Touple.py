
t3 = (1, "Python", 3.14, True)
t4 = (100,)          # Single-element tuple (comma required)

print("t3:", t3)
print("t4:", t4)

# indexing allowed
print(t3[2])
print(t3[-2])

# Concatenation
new_tpl = t4 + (60, 70)
print(new_tpl)

# Repetition works like list
print(("Hi",) * 3)

# count() Method
print("\ncount()")
numbers = (1, 2, 2, 3, 2, 4, 5)
print(numbers.count(2))

# index() Method
print(numbers.index(3))

print("\nBuilt-in Functions")
nums = (5, 10, 15, 20)

print("Max:", max(nums))
print("Min:", min(nums))
print("Sum:", sum(nums))
print("Sorted:", sorted(nums))
print("Any:", any((0, False, 5)))
print("All:", all((1, True, 5)))

# -------------------------
# Packing
# -------------------------
print("\nPacking")
person = ("Nayan", 21, "India")
print(person)

# Unpacking
print("\nUnpacking")
name, age, country = person
print(name)
print(age)
print(country)

# Extended Unpacking
print("\nExtended Unpacking")
a, *b, c = (1, 2, 3, 4, 5)
print(a)
print(b)
print(c)

# Nested Tuple
print("\nNested Tuple")
nested = ((1, 2), (3, 4), (5, 6))
print(nested[1])
print(nested[1][0])

# Converting Tuple
print("\nConversions")
list_data = list(t1)
print(list_data)

tuple_data = tuple(list_data)
print(tuple_data)

# Deleting Entire Tuple
print("\nDeleting Tuple")
temp = (100, 200, 300)
print(temp)
del temp
# print(temp)   # NameError (tuple deleted)

# Useful Examples
print("\nUseful Examples")

# Enumerate
print("\nEnumerate")
for index, value in enumerate(marks):
    print(index, value)

# Zip
print("\nZip")
names = ("Ram", "Shyam", "Mohan")
scores = (90, 85, 95)

for data in zip(names, scores):
    print(data)