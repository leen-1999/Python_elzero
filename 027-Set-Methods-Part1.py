# -----------------
# -- Set Methods --
# -----------------

# clear()

a = {1, 2, 3}
a.clear()
print(a)

# union()

b = {"One", "Two", "Three"}
c = {"1", "2", "3"}
x = {"Zero", "Cool"}

print(b | c)
print(b.union(c, x))

# add()

d = {1, 2, 3, 4}
d.add(5) # takes one parameter only
d.add(6)
print(d)

# copy() shallow copy 

e = {1, 2, 3, 4}
f = e.copy()

print(e)
print(f)

e.add(6)

print(e)
print(f)

# remove()

g = {1, 2, 3, 4}
g.remove(1)
# g.remove(7) # key error
print(g)

# discard()

h = {1, 2, 3, 4}
h.discard(1)
h.discard(7) #unlike remove, discard doesn't give error when the element it is not found
print(h)

# pop()

i = {"A", True, 1, 2, 3, 4, 5}
print(i.pop()) # remove randomly

# update() udate a set with the unionof itself and others

j = {1, 2, 3}
k = {1, "A", "B", 2}
j.update(['Html', "Css"]) # can update with list
j.update(k)

print(j)

