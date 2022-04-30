# ---------------------
# -- Strings Methods --
# ---------------------

# replace(Old Value, New Value, Count)

a = "Hello One Two Three One One"
print(a.replace("One", "1")) # replace the all ones 
print(a.replace("One", "1", 1))
print(a.replace("One", "1", 2))

# join(Iterable) iterable option to be able to loop over (tuple/list)

myList = ["Osama", "Mohamed", "Elsayed"]
print("-".join(myList)) # give a seprator as parameter to seprate elemnets in string 
print(" ".join(myList))
print(", ".join(myList))
print(type(", ".join(myList)))