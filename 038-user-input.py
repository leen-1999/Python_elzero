# ----------------
# -- User Input --
# ----------------

# / backslash to scape single or doble quotes in the  string
fName = input('What\'s Is Your First Name?')
mName = input('What\'s Is Your Middle Name?')
lName = input('What\'s Is Your Last Name?')
# if we don't use strip method the spaces when we input on console will be hold when we print
# print(f"Hello {fName} {mName:.1s} {lName} Happy To See You.")
fName = fName.strip().capitalize()  # chain methods
mName = mName.strip().capitalize()
lName = lName.strip().capitalize()

# {mName:.1s}
print(f"Hello {fName} {mName:.1s} {lName} Happy To See You.")
