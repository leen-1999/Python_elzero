# assign 01


class Game:
    def __init__(self, name, developer, year, price):
        self.name = name
        self.developer = developer
        self.year = year
        self.price = price

    def price_in_pounds(self):
        return self.price * 15.6


game_one = Game("Ys", "Falcom", 2010, 50)

print(f"Game Name Is \"{game_one.name}\", ", end="")
print(f"Developer Is \"{game_one.developer}\", ", end="")
print(f"Release Date Is \"{game_one.year}\", ", end="")
print(f"Price In Egypt Is {game_one.price_in_pounds()}", end="")


# assign 02

class User:
    def __init__(self, fname, sname, age, gender):
        self.fname = fname
        self.sname = sname
        self.age = age
        self.gender = gender

    def full_details(self):
        if self.gender == "Male":
            return f"Hello Mr {self.fname} {self.sname[0]}. [{str(40 - self.age).zfill(2) }] Years To Reach 40"
        elif self.gender == "Female":
            return f"Hello Mrs {self.fname} {self.sname[0]}. [{str(40 - self.age).zfill(2) }] Years To Reach 40"


user_one = User("Osama", "Mohamed", 38, "Male")
user_two = User("Eman", "Omar", 25, "Female")

print(user_one.full_details())  # Hello Mr Osama M. [02] Years To Reach 40
print(user_two.full_details())  # Hello Mrs Eman O. [15] Years To Reach 40

#  assign. 03


class Message:
    @staticmethod
    def print_message():
        return f"Hello From Class Message"


print(Message.print_message())

# Output
# Hello From Class Message

# assign 04 ???


class Games:
    def __init__(self, one_name="", nList=[], count=None):
        self.one_name = one_name
        self.nList = nList
        self.count = count

    def __init__(self, nList):

        self.nList = [nList]
        self.one_name = ""
        self.count = -1

    def __init__(self, count):
        self.count = count
        self.nList = []
        self.one_name = ""

    def set_name(self, gName):
        if gName not in self.nList:
            self.nList.append(gName)

    def show_games(self):
        if len(self.one_name) != 0:
            return f" I Have One Game Called \"{self.one_name}\""
        elif len(self.nList) != 0:
            print(" I Have Many Games: ")
            for element in self.nList:
                print("-- " + self.nList[element])
        elif self.count >= 0:
            return f"I Have {self.count} Game."


my_game = Games("Shadow Of Mordor")
my_games_names = Games(["Ys II", "Ys Oath In Felghana", "YS Origin"])
my_games_count = Games(80)

my_game.show_games()
# Ouput
# I Have One Game Called "Shadow Of Mordor"

my_games_names.show_games()
# Ouput
# I Have Many Games:
# -- Ys II
# -- Ys Oath In Felghana
# -- YS Origin

my_games_count.show_games()
# Output
# I Have 80 Game.

# assign 05 inheritance'i baska bir sekilde nasil yapilir
#
# # Main Class


class Members:

    def __init__(self, n, p):

        self.name = n

        self.permission = p

    def show_info(self):

        return f"Your Name Is {self.name} And You Are {self.permission}"

# Create Admin Class Here


class Admins(Members):
    pass
# Create Moderators Class Here


class Moderators(Members):
    pass


member_one = Admins("Osama", "Admin")
member_two = Moderators("Ahmed", "Moderator")

print(member_one.show_info())
# Output
# Your Name Is Osama And You Are Admin

print(member_two.show_info())
# Output
# Your Name Is Ahmed And You Are Moderator


#   assign 06
class A:

    def __init__(self, one):

        self.one = one


class B:

    def __init__(self, two):

        self.two = two


class C:

    def __init__(self, three):

        self.three = three

# Write The Class Called "Text" Here


class Text():
    def __init__(self, one="", two="", three=""):
        self.one = one
        self.two = two
        self.three = three

    def show_name(self):
        return f" The Name Is {self.one+self.two+self.three}"


class Name(A, B, C):
    pass


the_name = Text("El", "ze", "ro")

print(the_name.show_name())

# Ouput
# The Name Is Elzero
