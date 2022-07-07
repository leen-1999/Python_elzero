# ---------------------------
# -- Break, Continue, Pass --
# ---------------------------

myNumbers = [1, 2, 3, 5, 7, 10, 13, 14, 15, 19]

# Continue

for number in myNumbers:

    if number == 13:

        continue

    print(number)

print("#" * 50)

# Break

for number in myNumbers:

    if number == 13:

        break

    print(number)

print("#" * 50)

# Pass

for number in myNumbers:

    if number == 13:

        pass  # empty function/loop/condition where will give error if it's empty

    print(number)
