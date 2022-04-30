# -------------
# -- Strings --
# -------------

myStringOne = 'This is Single Quote'
myStringTwo = "This is Double Quotes"

print(myStringOne)
print(myStringTwo)

# if you want to print with quotes single/double without using escape \ like in previous lecture
myStringThree = 'This is Single Quote "Test"'
myStringFour = "This is Double Quotes 'Test'"

print(myStringThree)
print(myStringFour)

# if you want to print multiple lines you can use triple single/double quotes
# ayni zamanda triple single/double quotes quotes icinde bastirmek istedigimizi yani ozel quote karakterini es gecer oldugu gib yazdirir
myStringFive = '''First
Second 'Test' "Test"
Third'''

myStringSix = """First
Second "Test" \\\ 'Test'
Third"""

print(myStringFive)
print(myStringSix)
