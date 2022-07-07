# ----------------------------------
# -- Date and Time => Format Date --
# ----------------------------------
# https://strftime.org/   # python's strftime directives
# ---------------------

import datetime

myBirthday = datetime.datetime(1982, 10, 25)

print(myBirthday)
# strftime => string format time returns formatted time as string
print(myBirthday.strftime("%a"))
print(myBirthday.strftime("%A"))
print(myBirthday.strftime("%b"))
print(myBirthday.strftime("%B"))

# Y => the complete year 1982 where y => 82
print(myBirthday.strftime("%d %B %Y"))
print(myBirthday.strftime("%d, %B, %Y"))
print(myBirthday.strftime("%d/%B/%Y"))
print(myBirthday.strftime("%d - %B - %Y"))
print(myBirthday.strftime("%B - %Y"))
