# -------------------
# -- File Handling --
# -------------------
# "a" Append  Open File For Appending Values, Create File If Not Exists
# "r" Read    [Default Value] Open File For Read and Give Error If File is Not Exists
# "w" Write   Open File For Writing, Create File If Not Exists
# "x" Create  Create File, Give Error If File Exists
# --------------------------------------------------

# There are two types of paths/ directories
# one is the absolute path (it starts rout from computer until the current file) it is more guranteed
# the other is the realtive path (it is realted with the current place)


import os

# Main Current Working Directory(cwd)
print(os.getcwd())

# Directory For The Opened File
print(os.path.dirname(os.path.abspath(__file__)))

# Change Current Working Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print(os.getcwd())

print(os.path.abspath(__file__))

# r means that is row string don't care with anu commnad inside like \n
file = open(r"D:\Python\Files\nfiles\osama.txt")

file = open("D:\Python\Files\osama.txt")
