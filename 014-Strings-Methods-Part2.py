# ---------------------
# -- Strings Methods --
# ---------------------

# split() rsplit()
# split datayi alip  boler listeye donusturur
# split iki parametre alabilir seprator ve max split

a = "I Love Python and PHP and MySQL"
# default olarak spacelere gore liste elemanlarina ayiriyor
print(a.split())
print("=" * 50)
b = "I-Love-Python-and-PHP-and-MySQL"
print(b.split("-"))
print("=" * 50)
c = "I-Love-Python-and-PHP-and-MySQL"
print(c.split("-", 3))
print("=" * 50)
d = "I-Love-Python-and-PHP-and-MySQL"
print(d.rsplit("-", 3))
print("=" * 50)
# center()
# karakter ekler
e = "Osama"
print(e.center(9))  # Spaces
print("=" * 50)
print(e.center(9, "#"))  # Hashes
print("=" * 50)
print(e.center(15, "@"))  # @

# count()

f = "I Love Python and PHP Because PHP is Easy"
# 2 PHP Words but be ware about case sensitive for letters PHP is different from php
print(f.count("PHP"))
print("=" * 50)
print(f.count("PHP", 0, 25))  # Only One PHP Word
print("=" * 50)
# swapcase()
# convert every letter in string from capital to small and vice versa

g = "I Love Python"
h = "i lOVE pYTHON"

print(g.swapcase())
print("=" * 50)
print(h.swapcase())
print("=" * 50)

# startswith()

i = "I Love Python"
print(i.startswith("I"))
print("=" * 50)
print(i.startswith("S"))
print("=" * 50)
print(i.startswith("P", 7, 12))
print("=" * 50)

# endswith()

j = "I Love Python"
print(j.endswith("n"))
print("=" * 50)
print(j.endswith("S"))
print("=" * 50)
print(j.endswith("e", 2, 6))  # exculding the end  --> 6
print("=" * 50)
