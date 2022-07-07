# ------------------------
# -- Built In Functions --
# ------------------------
# sum()
# round()
# range()
# print()
# ------------------------

# sum(iterable, start) # iterable is mendatory when start is optional and it is zero by default
a = [1, 10, 19, 40]
print(sum(a))
print(sum(a, 40))

# round(number, numofdigits)
# if the fractional part is above the half the result is 151 if it is not 150
print(round(150.501))
print(round(150.554, 2))

# range(start, end, step) # end is mendatory when the others are optional
print(list(range(0)))
print(list(range(10)))
print(list(range(0, 20, 2)))

# print()
print("Hello @ Osama @ How @ Are @ You")
# comma means that you have more than one message respectively
# when there is no sep the default value is sapce
print("Hello", "Osama", "How", "Are", "You", sep=" | ")

# the defaul value for end is \n end="\n" or just print("First Line")
print("First Line", end=" ")
print("Second Line")
print("Third Line")
