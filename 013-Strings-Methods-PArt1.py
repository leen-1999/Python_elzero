# ---------------------
# -- Strings Methods --
# ---------------------

# strip() rstrip() right strip  lstrip() left strip

# sag ve soldaki mesafeleri kaldirir, sagdaki, soldaki measafeleri kaldirir 
a = "    I Love Python    "
print(a.strip())
print(a.rstrip())
print(a.lstrip())

a = "#####I Love Python####"
print(a.strip("#"))
print(a.rstrip("#"))
print(a.lstrip("#"))

a = "@#@#@#I Love Python@#@#@#"
print(a.strip("@#"))
print(a.rstrip("@#"))
print(a.lstrip("@#"))

# title()
# her kelimenin ilk harfini ve sayilardan sonraki harfleri buyuk yapar
b = "I Love 2d Graphics and 3g Technology and python"
print(b.title())

# capitalize()
# her kelimenin ilk harfini buyuk yapar
b = "I Love 2d Graphics and 3g Technology and python"
print(b.capitalize())

# zfill

c, d, e, f = "1", "11", "111", "1111"

print(c)
print(d)
print(e)
print(f)
 
# fill with zeros on the left 
# 4 basamkali  sayi dondurur sifirlarla doldurur soldaki bos basamklari
print(c.zfill(4))
print(d.zfill(4))
print(e.zfill(4))
print(f.zfill(4))

# upper()

g = "osama"

print(g.upper())

# lower()

h = "OSama"

print(h.lower())



# len() 