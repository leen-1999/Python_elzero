# -------------------
# -- Concatenation --
# -------------------

msg = "I Love"
lang = "Python"
print(msg + lang) #  print without space
print(msg + " " + lang)

full = msg + " " + lang
print(full)

a = "First \
Second \
Third"

b = "A \
B \
C"

print(a + " " + b)
print(a + "\n" + b)
print("Hello\nWorld") # print(a\nb) gives error 

print("Hello " + 1)  # Error