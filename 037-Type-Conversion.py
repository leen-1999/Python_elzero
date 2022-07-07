# ---------------------
# -- Type Conversion --
# ----------------------

# str()

a = 10
print(type(a))
print(type(str(a)))

print("#" * 50)

# tuple()
# to convert to tuple the converted element must be iterable
# you can't convert int to tuple since it is not an iterable object
c = "Osama"  # String
d = [1, 2, 3, 4, 5]  # List
e = {"A", "B", "C"}  # Set  return an unordered elements
f = {"A": 1, "B": 2}  # Dictionary

print(tuple(c))
print(tuple(d))
print(tuple(e))  # returns an unrderd tuple
print(tuple(f))  # the keys only

# list()

c = "Osama"  # String
d = (1, 2, 3, 4, 5)  # Tuple
e = {"A", "B", "C"}  # Set
f = {"A": 1, "B": 2}  # Dictionary

print(list(c))
print(list(d))
print(list(e))
print(list(f))

print("#" * 50)

# set()

c = "Osama"  # String
d = (1, 2, 3, 4, 5)  # Tuple
e = ["A", "B", "C"]  # List
f = {"A": 1, "B": 2}  # Dictionary

print(set(c))
print(set(d))
print(set(e))
print(set(f))

print("#" * 50)

# dict()

d = (("A", 1), ("B", 2), ("C", 3))  # Tuple # nested tuples as key and value
# List # the same idea but this doesn't work with set since it is not hashable
e = [["One", 1], ["Two", 2], ["Three", 3]]

print(dict(d))
print(dict(e))
