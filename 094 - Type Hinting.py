# ------------------
# -- Type Hinting --
# ------------------


# -> str/int/float/list

def say_hello(name) -> str:

    print(f"Hello {name}")


say_hello("Ahmed")


def calculate(n1, n2) -> list:

    print(n1 + n2)


calculate(10, 40)
