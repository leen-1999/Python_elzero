# -------------------------
# -- Decorators => Intro --
# -------------------------
# [1] Sometimes Called Meta Programming
# [2] Everything in Python is Object Even Functions
# [3] Decorator Take A Function and Add Some Functionality and Return It
# [4] Decorator Wrap Other Function and Enhance Their Behaviour
# [5] Decorator is Higher Order Function (Function Accept Function As Parameter) and return a function
# ----------------------------------------------------------------------

def myDecorator(func):  # Decorator

    def nestedFunc():  # Any Name Its Just For Decoration

        print("Before")  # Message From Decorator

        func()  # Execute Function

        print("After")  # Message From Decorator

    return nestedFunc  # Return All Data

# the first way => is to use @myDecorator


@myDecorator  # it works only with the next func defined
# we have to write the above line before every func we will use
# the decorator with
def sayHello():

    print("Hello From Say Hello Function")


sayHello()


@myDecorator
def sayHowAreYou():

    print("Hello From Say How Are You Function")


# the second way
afterDecoration = myDecorator(sayHello)

afterDecoration()


print("#" * 50)

sayHowAreYou()
