# ---------------
# -- Nested If --
# ---------------

uName = "Osama"
isStudent = "Yes"
uCountry = "Egypt"
cName = "Python Course"
cPrice = 100

if uCountry == "Egypt" or uCountry == "KSA" or uCountry == "Qatar":

    if isStudent == "Yes":

        print(f"Hi {uName} Because U R From {uCountry} And Student")
        print(f"The Course \"{cName}\" Price Is: ${cPrice - 90}")

    else:

        print(f"Hi {uName} Because U R From {uCountry}")
        print(f"The Course \"{cName}\" Price Is: ${cPrice - 80}")

elif uCountry == "Kuwait" or uCountry == "Bahrain":

    print(f"Hi {uName} Because U R From {uCountry}")
    print(f"The Course \"{cName}\" Price Is: ${cPrice - 50}")

else:
    print(f"Hi {uName} Because U R From {uCountry}")
    print(f"The Course \"{cName}\" Price Is: ${cPrice - 30}")
