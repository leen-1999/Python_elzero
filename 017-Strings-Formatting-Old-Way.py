# ------------------------
# -- Strings Formatting --
# ------------------------

name = "Osama"
age = 36
rank = 10

print("My Name is: " + name)
print("My Name is: " + name + " and My Age is: " + age)  # Type Error
# because we can't concatenate string with number by + operator
# Exception has occurred: TypeError
#can only concatenate str (not "int") to str

# %s placeholder for strings
# %d placeholder for numbers
print("My Name is: %s" % "Osama") # Osama is the value will hold in place of %s
print("My Name is: %s" % name) # the vale of variable (name)  is the value will hold in place of %s
print("My Name is: %s and My Age is: %d" % (name, age))
print("My Name is: %s and My Age is: %d and My Rank is: %f" % (name, age, rank))

# %s => String
# %d => Number
# %f => Floating point number

n = "Osama"
l = "Python"
y = 10

print("My Name is %s Iam %s Developer With %d Years Exp" % (n, l, y))

# Control Floating Point Number

myNumber = 10
print("My Number is: %d" % myNumber)
print("My Number is: %f" % myNumber)
print("My Number is: %.2f" % myNumber) # vigulden sonra 2 basamk koyar 

# Truncate String / Slice string
# bir stringden istemediklerimi cikartip istedigimi birakmak icin

myLongString = "Hello People of Elzero Web School I Love You All"
print("Message is %s" % myLongString)
print("Message is %.5s" % myLongString) # myLongStringin ilk 5 harfini gosterir 1'den saymaya baslar 
# yani H --> 1
# e --> 2
# l __> 3