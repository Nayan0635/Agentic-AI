# Creating dictionaries
d = {"name": "Nayan", "age": 20, "city": "Kolkata"}
print(d)
# Output: {'name': 'Nayan', 'age': 20, 'city': 'Kolkata'}

d2 = dict(id=101, marks=95)
print(d2)
# Output: {'id': 101, 'marks': 95}

# Accessing value
print(d["name"])
# Output: Nayan

print(d.get("age"))
# Output: 20

# Returns default value if key is not present
print(d.get("salary", 0))
# Output: 0

# Adding new key-value pair
d["gender"] = "Male"
print(d)
# Output: {'name': 'Nayan', 'age': 20, 'city': 'Kolkata', 'gender': 'Male'}

# Updating existing value
d["age"] = 21
print(d)
# Output: {'name': 'Nayan', 'age': 21, 'city': 'Kolkata', 'gender': 'Male'}

# Updates multiple key-value pairs
d.update({"city": "Delhi", "salary": 50000})
print(d)
# Output: {'name': 'Nayan', 'age': 21, 'city': 'Delhi', 'gender': 'Male', 'salary': 50000}

# Removes specified key and returns its value
x = d.pop("salary")
print(x)
print(d)
# Output:
# 50000
# {'name': 'Nayan', 'age': 21, 'city': 'Delhi', 'gender': 'Male'}

# Removes last inserted key-value pair
y = d.popitem()
print(y)
print(d)
# Output:
# ('gender', 'Male')
# {'name': 'Nayan', 'age': 21, 'city': 'Delhi'}

# Removes specified key
del d["city"]
print(d)
# Output: {'name': 'Nayan', 'age': 21}

# Removes all key-value pairs
temp = {"a": 1, "b": 2}
temp.clear()
print(temp)
# Output: {}

# Returns all keys
print(d.keys())
# Output: dict_keys(['name', 'age'])

# Returns all values
print(d.values())
# Output: dict_values(['Nayan', 21])

# Returns all key-value pairs
print(d.items())
# Output: dict_items([('name', 'Nayan'), ('age', 21)])

# Creates a separate copy
copy_dict = d.copy()
print(copy_dict)
# Output: {'name': 'Nayan', 'age': 21}

# Length
print(len(d))
# Output: 2

# Checks if key is present
print("name" in d)
# Output: True

print("city" in d)
# Output: False

# Iterating through keys
for key in d:
    print(key)
# Output:
# name
# age

# Iterating through values
for value in d.values():
    print(value)
# Output:
# Nayan
# 21

# Iterating through key-value pairs
for key, value in d.items():
    print(key, value)
# Output:
# name Nayan
# age 21

# Creates dictionary with same default value
nums = dict.fromkeys(["a", "b", "c"], 0)
print(nums)
# Output: {'a': 0, 'b': 0, 'c': 0}

# Inserts key if absent
person = {"name": "Rahul"}
print(person.setdefault("age", 20))
print(person)
# Output:
# 20
# {'name': 'Rahul', 'age': 20}

# Does not change existing value
print(person.setdefault("name", "Amit"))
print(person)
# Output:
# Rahul
# {'name': 'Rahul', 'age': 20}