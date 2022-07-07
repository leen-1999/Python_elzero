# ---------------------------------
# -- Modules => Built In Modules --
# ---------------------------------
# [1] Module is A File Contain A Set Of Functions
# [2] You Can Import Module in Your App To Help You
# [3] You Can Import Multiple Modules
# [4] You Can Create Your Own Modules
# [5] Modules Saves Your Time
# --------------------------------------------------

# Import Main Module

from random import randint, random
import random
print(random)
# modulname.functionName()
print(f"Print Random Float Number {random.random()}")

# Show All Functions Inside Module
print(dir(random))

# Import One Or Two Functions From Module
# from random import randint, random
# from random import * bring all the functions inside the module
# from moduleName import functionName
# since we didn't import the whole module but just a specific functions
# so we can't say random.randint(100,900)
print(f"Print Random Float {random()}")
print(f"Print Random Integer {randint(100, 900)}")
