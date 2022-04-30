# ---------------------
# -- Strings Methods --
# ---------------------

# index(SubString, Start, End)
# susbstring is oblgatory part  when start and end are optional

a = "I Love Python"
# print(a.index("P"))  # Index Number 7
# print(a.index("P", 0, 10))  # Index Number 7
# print(a.index("P", 0, 5))  # Through Error

# find(SubString, Start, End)
# unlike with index method find method when the substrinf
# is not found it doesn't give error and stops excuting code
# it gives just -1

b = "I Love Python"
print(b.find("P"))  # Index Number 7
print(b.find("P", 0, 10))  # Index Number 7
print(b.find("P", 0, 5))  # -1

# rjust(Width, Fill Char) ljust(Width, Fill Char)
# right justified , left justified
# width is the full  umber of returned characters

c = "Osama"
print(c.rjust(10))  # adds spaces on the left
print(c.rjust(10, "#"))

d = "Osama"
print(d.ljust(10))  # adds spaces on the right
print(d.ljust(10, "#"))

# splitlines()
# returns every line as elemnt in list

e = """First Line
Second Line
Third Line"""

print(e.splitlines())

f = "First Line\nSecond Line\nThird Line"

print(f.splitlines())

# expandtabs()

g = "Hello\tWorld\tI\tLove\tPython"
print(g.expandtabs(2))

# istitle()

one = "I Love Python And 3G"
two = "I Love Python And 3g"
print(one.istitle())  # true
print(two.istitle())  # false 3g g is small

# isspace()

three = " "
four = ""
print(three.isspace())
print(four.isspace())

# islower()

five = 'i love python'
six = 'I Love Python'
print(five.islower())
print(six.islower())

# isidentifier()  is it suitable to be variable name

seven = "osama_elzero"
eight = "OsamaElzero100"
nine = "Osama--Elzero100"

print(seven.isidentifier())
print(eight.isidentifier())
print(nine.isidentifier())

# isalpha() is it alphabatical string (alphabatical string contains from a to z or A to Z)

x = "AaaaaBbbbbb"
y = "AaaaaBbbbbb111"
print(x.isalpha())
print(y.isalpha())

# isalnum return true if alpha/num/alpha + num

u = "AaaaaBbbbbb"
z = "AaaaaBbbbbb111"
print(u.isalnum())  # false
print(z.isalnum())  # true
