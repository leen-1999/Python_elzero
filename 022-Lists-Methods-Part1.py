# -------------------
# -- Lists Methods --
# -------------------

# append()

myFriends = ["Osama", "Ahmed", "Sayed"]
myOldFriends = ["Haytham", "Samah", "Ali"]

myFriends.append("Alaa")
myFriends.append(100)
myFriends.append(150.200)
myFriends.append(True)
myFriends.append(myOldFriends) # adds the list as one element

print(myFriends)
print(myFriends[2])
print(myFriends[6])
print(myFriends[7]) # access the whole list since it behaves as a one element
print(myFriends[7][2]) # to access an element inside that list (inner one) 

# extend()

a = [1, 2, 3, 4]
b = ["A", "B", "C"]
c = ["One", "Two"]

a.extend(b) # unlike append method, b will not be added as a one elment 
a.extend(c)

print(a)

# remove()

x = [1, 2, 3, 4, 5, "Osama", True, "Osama", "Osama"]
x.remove("Osama") # remove Osama at the first appearance and let the others  
print(x)

# sort() 
# in sort the list must contain one type elements

y = [1, 2, 100, 120, -10, 17, 29]
# y = ["A", "Z", "C"]
# y.sort() sorts in increasing order since the dafault sate is y.sort(reverse=False)
y.sort(reverse=True) # sorts in decreasing order
print(y)

# reverse()
# the list can contains different types inside

z = [10, 1, 9, 80, 100, "Osama", 100]
z.reverse()
print(z)
