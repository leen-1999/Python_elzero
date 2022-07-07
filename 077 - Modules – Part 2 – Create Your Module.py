# -----------------------------------
# -- Modules => Create Your Module --
# -----------------------------------

from elzero import sayHello as ss
from elzero import sayHello
import elzero as ee
import elzero
import sys
sys.path.append(r"D:\Games")
print(sys.path)  # bring python system's paths searching the module to be imported

print(dir(elzero))

elzero.sayHello("Ahmed")
elzero.sayHello("Osama")
elzero.sayHello("Mohamed")

elzero.sayHowAreYou("Ahmed")
elzero.sayHowAreYou("Osama")
elzero.sayHowAreYou("Mohamed")


# Alias
# import elzero as ee

ee.sayHello("Ahmed")
ee.sayHello("Osama")
ee.sayHello("Mohamed")

ee.sayHowAreYou("Ahmed")
ee.sayHowAreYou("Osama")
ee.sayHowAreYou("Mohamed")

# from elzero import sayHello
sayHello("Osama")

# from elzero import sayHello as ss
ss("Osama")
