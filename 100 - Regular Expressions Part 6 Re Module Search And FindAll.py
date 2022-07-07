# ---------------------------------------------------------
# -- Regular Expressions => Re Module Search And FindAll --
# ---------------------------------------------------------
# search()  => Search A String For A Match And Return A First Match Only
# findall() => Returns A List Of All Matches and Empty List if No Match
# ---------------------------------------------------------------------
# Email Pattern => [A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)
# ----------------------------------------------------------

import re

# r provides not understanding another thing of reg. exp.
my_search = re.search(r"[A-Z]{2}", "OOsamaEElzero")

# sapan returns the index of the matched pattern
print(my_search)
# if we worry the methods inside search() print(dir(my_search)
print(my_search.span())
print(my_search.string)  # the string you search for
print(my_search.group())

is_email = re.search(r"[A-z0-9\.]+@[A-z0-9]+\.(com|net)", "os@osama.com")

if is_email:

    print("This is A Valid Email")

    print(is_email.span())
    print(is_email.string)
    print(is_email.group())  # returns the matched pattern

else:

    print("This is Not A Valid Email")

email_input = input("Please Write Your Email: ")

search = re.findall(r"[A-z0-9\.]+@[A-z0-9]+\.com|net", email_input)

empty_list = []

if search != []:

    empty_list.append(search)

    print("Email Added")

else:

    print("Invalid Email")

for email in empty_list:

    print(email)
