# ------------------------------------------------------
# -- Regular Expressions => Group Trainings And Flags --
# ------------------------------------------------------
# . matches any character except \n --> new line

import re

my_web = "https://www.elzero.org:8080/category.php?article=105?name=how-to-do"

# search = re.search(r"(https?)://(www)?\.?(\w+)\.(\w+):?(\d+)?/?(.+)", my_web,re.m) # flag re.m multiline, re.DOTALL . matches any character including newline\ re.I ignorecase cpitalsmall letters

search = re.search(r"(https?)://(www)?\.?(\w+)\.(\w+):?(\d+)?/?(.+)", my_web)

# returns the complete searched pattern since we didn't give the group number
print(search.group())
# returns matched pattern as groups(all of groups separatly) if not mathced returns none so there a need to control
print(search.groups())

for group in search.groups():

    print(group)

print(f"Protocol: {search.group(1)}")
print(f"Sub Domain: {search.group(2)}")
print(f"Domain Name: {search.group(3)}")
print(f"Top Level Domain: {search.group(4)}")
print(f"Port: {search.group(5)}")
print(f"Query String: {search.group(6)}")
