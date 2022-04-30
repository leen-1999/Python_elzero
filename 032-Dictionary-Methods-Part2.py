# ------------------------
# -- Dictionary Methods --
# ------------------------

# setdefault() if it founds the key you give it returns the value of it
# exists in the dict if the key it is not found it will add the new key with its value which you gave
# if you don't give a value just a key it will give none for value

user = {
    "name": "Osama"
}
print(user)
print(user.setdefault("age", 36))
print(user)

print("=" * 40)

# popitem() remove and the return the last element you added to the dictionary

member = {
    "name": "Osama",
    "skill": "PS4"
}
print(member)
member.update({"age": 36})
print(member.popitem())
print(member)

print("=" * 40)

# items() holds the changes also

view = {
    "name": "Osama",
    "skill": "XBox"
}

allItems = view.items()
print(view)
view["age"] = 36

print(allItems)

print("=" * 40)

# fromkeys()

a = ('MyKeyOne', 'MyKeyTwo', 'MyKeyThree')
b = "X"

print(dict.fromkeys(a, b))
