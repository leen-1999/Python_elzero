# ---------------------------
# -- Dictionary --
# ----------------
# [1] Dict Items Are Enclosed in Curly Braces
# [2] Dict Items Are Contains Key : Value
# [3] Dict Key Need To Be Immutable => (Number, String, Tuple) List Not Allowed
# [4] Dict Value Can Have Any Data Types
# [5] Dict Key Need To Be Unique if you put the same key more than one time it will takes the last value for it
# [6] Dict Is Not Ordered You Access Its Element With Key
# ----------------------------

# Dictionary

user = {
    "name": "Osama",
    "age": 36,
    "country": "Egypt",
    "skills": ["Html", "Css", "JS"],
    "rating": 10.5
}

print(user)
print(user['country'])
print(user.get("country"))

print(user.keys())
print(user.values())

# Two-Dimensional Dictionary / nested dictionary

languages = {
    "One": {
        "name": "Html",
        "progress": "80%"
    },
    "Two": {
        "name": "Css",
        "progress": "90%"
    },
    "Three": {
        "name": "Js",
        "progress": "90%"
    }
}

print(languages)
print(languages['One'])
print(languages['Three']['name'])

# Dictionary Length

print(len(languages))
print(len(languages["Two"]))

# Create Dictionary From Variables

frameworkOne = {
    "name": "Vuejs",
    "progress": "80%"
}

frameworkTwo = {
    "name": "ReactJs",
    "progress": "80%"
}

frameworkThree = {
    "name": "Angular",
    "progress": "80%"
}

allFramework = {
    "one": frameworkOne,
    "two": frameworkTwo,
    "three":  frameworkThree
}

print(allFramework)
