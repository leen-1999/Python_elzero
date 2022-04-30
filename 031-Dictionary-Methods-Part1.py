# ------------------------
# -- Dictionary Methods --
# ------------------------

# clear()

user = {
    "name": "Osama"
}
print(user)
user.clear()
print(user)

print("=" * 50)

# update() we can update more than one value with its key in the same instruction

member = {
    "name": "Osama"
}
print(member)
member["age"] = 36  # add a new element without update method
print(member)
member.update({"country": "Egypt"})
print(member)

print("=" * 50)

# copy() shallow copy

main = {
    "name": "Osama"
}

b = main.copy()
print(b)
main.update({"skills": "Fighting"})
print(main)
print(b)

# keys() + values()

print(main.keys())
print(main.values())
