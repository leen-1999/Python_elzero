# -----------------------------
# -- Lists --
#it is not an array  but does the same thing with array
#to use array there a module we have to import to be able to use array 
# -----------
# [1] List Items Are Enclosed in Square Brackets
# [2] List Are Ordered, To Use Index To Access Item
# [3] List Are Mutable => Add, Delete, Edit
# [4] List Items Is Not Unique
# [5] List Can Have Different Data Types
# -----------------------------

myAwesomeList = ["One", "Two", "One", 1, 100.5, True]

print(myAwesomeList)  # Whole List
print(myAwesomeList[1])  # "Two"
print(myAwesomeList[-1])  # True
print(myAwesomeList[-3])  # 1

# slice
print(myAwesomeList[1:4])  # ['Two', 'One', 1]
print(myAwesomeList[:4])  # ['One', 'Two', 'One', 1]
print(myAwesomeList[1:])  # ['Two', 'One', 1, 100.5, True]

print(myAwesomeList[::1])  # ['One', 'Two', 'One', 1, 100.5, True]
print(myAwesomeList[::2])  # ['One', 'One', 100.5]

print(myAwesomeList)
# myAwesomeList[1] = 2
# myAwesomeList[-1] = False
# in list we can edit/reassign  more than  one element at the same time
# myAwesomeList[0:3] = [] bu sekilde yazarsak ordaki elemamlari cikartir
# myAwesomeList[0:3] = ["A","B","C"]
# myAwesomeList[0:3] = ["A","B"]
# myAwesomeList[0:3] = ["A"]
myAwesomeList[0:3] = ["A"]
print(myAwesomeList)
