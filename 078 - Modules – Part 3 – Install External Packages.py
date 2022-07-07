# ------------------------------------------
# -- Modules => Install External Packages --
# ------------------------------------------
# [1] Module vs Package : module is a single file contains functions does the  rquired idea where the package is a set of modules
# [2] External Packages Downloaded From The Internet
# [3] You Can Install Packages With Python Package Manager PIP
# [4] PIP Install the Package and Its Dependencies
# [5] Modules List "https://docs.python.org/3/py-modindex.html"
# [6] Packages and Modules Directory "https://pypi.org/"
# [7] PIP Manual "https://pip.pypa.io/en/stable/reference/pip_install/"
# ---------------------------------------------------------------------


# to check if you have pip or not write on terminal pip --version
# python --version
# pip list
# pip install packageName/moduleName
# pip install termcolor
# pip install pyfiglet
# pip install modulename modulename modulename # to install multiple modules
# to install a specific version pip install pyfiglet==1.0.4
# or pip install pyfiglet>=1.0.4
# to update package => pip install pip --upgrade
# if there is a problem  with user permision write pip install --user pip --upgrade

import termcolor
import pyfiglet

print(dir(pyfiglet))
print(pyfiglet.figlet_format("Elzero"))  # converts the string to asci art
print(termcolor.colored("Elzero", color="yellow"))
# if you want to know the satisfied colors write help termcolor #help(termcolor)
print(termcolor.colored(pyfiglet.figlet_format("Elzero"), color="yellow"))
