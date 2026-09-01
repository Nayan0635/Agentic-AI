# Creating sets
s = {10, 20, 30, 40}
print(s)
# Output: {40, 10, 20, 30}

s2 = set([1, 2, 3, 2, 1])
print(s2)
# Output: {1, 2, 3}

# add
s.add(50)
print(s)
# Output: {40, 10, 50, 20, 30}

# Adds multiple elements
s.update([60, 70])
print(s)
# Output: {70, 40, 10, 50, 20, 60, 30}

# Removes if present, otherwise gives error
s.remove(20)
print(s)
# Output: {70, 40, 10, 50, 60, 30}

# Removes if present, otherwise does nothing
s.discard(100)
print(s)
# Output: {70, 40, 10, 50, 60, 30}

# Removes and returns any one element
x = s.pop()
print(x)
print(s)
# Output:
# 70
# {40, 10, 50, 60, 30}

# Removes all elements
temp = {1, 2, 3}
temp.clear()
print(temp)
# Output: set()

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Common elements
print(a.intersection(b))
# Output: {3, 4}

print(a & b)
# Output: {3, 4}

# All unique elements
print(a.union(b))
# Output: {1, 2, 3, 4, 5, 6}

print(a | b)
# Output: {1, 2, 3, 4, 5, 6}



# Present only in first set
print(a.difference(b))
# Output: {1, 2}

print(a - b)
# Output: {1, 2}

# Elements not common in both sets
print(a.symmetric_difference(b))
# Output: {1, 2, 5, 6}

print(a ^ b)
# Output: {1, 2, 5, 6}

# True if every element is present in another set
x = {1, 2}
y = {1, 2, 3, 4}

print(x.issubset(y))
# Output: True

# True if contains every element of another set
print(y.issuperset(x))
# Output: True

# True if no common elements
print({1, 2}.isdisjoint({3, 4}))
# Output: True

print({1, 2}.isdisjoint({2, 3}))
# Output: False

# Creates a separate copy
c = a.copy()
print(c)
# Output: {1, 2, 3, 4}

# Length
print(len(a))
# Output: 4

# Checks if present
print(3 in a)
# Output: True

print(10 in a)
# Output: False

# Iteration
for i in a:
    print(i)
# Output:
# 1
# 2
# 3
# 4

# Duplicate values are removed automatically
nums = {1, 2, 2, 3, 3, 4}
print(nums)
# Output: {1, 2, 3, 4}

# Frozen set (cannot be modified)
fs = frozenset([1, 2, 3])
print(fs)
# Output: frozenset({1, 2, 3})