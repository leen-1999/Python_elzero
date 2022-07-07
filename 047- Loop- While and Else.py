# -------------------
# -- Loop => While --
# -------------------
# while condition_is_true
#   Code Will Run Until Condition Become False
# -----------------------

a = 0

while a < 5:

    print(a)

    a += 1  # a = a + 1

print("Loop is Done")  # True Become False
# or we can write
# else:
# print("Loop is Done")  # True Become False

while False:

    print("Will Not Print")
