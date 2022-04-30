# -------------------
# -- Lists Methods --
# -------------------

# clear()

a = [1, 2, 3, 4]
a.clear()  # removes all items
print(a)

# copy()

b = [1, 2, 3, 4]
c = b.copy()

print(b)  # Main List
print(c)  # Copied List

b.append(5)

print(b)  # Main List
print(c)  # Copied List

# count()

d = [1, 2, 3, 4, 3, 9, 10, 1, 2, 1]
print(d.count(1))  # return the number of ones in the list

# index()

e = ["Osama", "Ahmed", "Sayed", "Ramy", "Ahmed", "Ramy"]
print(e.index("Ramy"))  # returns the index of elemnet at first appearance

# insert()

f = [1, 2, 3, 4, 5, "A", "B"]
f.insert(0, "Test")  # inserts the given object before the given index
f.insert(-1, "Test")

print(f)

# pop() remode and return item at index / index vermedigimoz zamanda listenin en sonundaki elemani kaldirir


g = [1, 2, 3, 4, 5, "A", "B"]
print(g.pop(-3))
print(g)
