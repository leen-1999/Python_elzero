
# ------------------------
# -- Built In Functions --
# ------------------------
# enumerate()
# help()
# reversed()
# ------------------------

# enumerate(iterable, start=0) # add a counter for iterable elements when being looped

mySkills = ["Html", "Css", "Js", "PHP"]

mySkillsWithCounter = enumerate(mySkills, 20)

print(type(mySkillsWithCounter))  # enumerate

for counter, skill in mySkillsWithCounter:

    print(f"{counter} - {skill}")

print("#" * 50)

# help()

print(help(print))

print("#" * 50)

# reversed(iterable)

myString = "Elzero"

print(reversed(myString))  # returns memory address
print(list(reversed(myString)))

myList = list(reversed(myString))
for letter in list(reversed(myString)):

    print(letter)

for letter in reversed(myString):

    print(letter)

for s in reversed(mySkills):

    print(s)
