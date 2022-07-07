def capitalize(string):
    newString = string.title()
    return newString


print(capitalize("osama elzero"))

print('#'*25)

the_name = "osama elzero"

# Split The Name To List Of Words
splitted = the_name.split(' ')  # Output => ['osama', 'elzero']

# Create Empty List To Add Words After Capitalize First Letter
all_words = []

# Loop On Words
for word in splitted:

    # Add Words After Capitalize First Letter
    all_words.append(word.capitalize())

# Join All Words in One String
joined = " ".join(all_words)

print(joined)

print('#'*25)

the_name = "osama elzero"

# Split The Name To List Of Words
splitted = the_name.split(' ')  # Output => ['osama', 'elzero']

# Join All Words in One String
joined = ' '.join((word.capitalize() for word in splitted))

print(joined)

print('#'*25)


def remove_space(string):
    # Split The Name To List Of Words
    splitted = string.split(' ')  # Output => ['osama', 'elzero']

    # Join All Words in One String
    joined = '-'.join((word.capitalize() for word in splitted))

    print(joined)


remove_space("osama elzero")

print('#'*25)

my_string = "Elzero Academy"

# Split Strings By Space Separator
splitted = my_string.split(" ")  # Ouput => ['Elzero', 'Academy']

# Join The List With Dash
joined = "-".join(splitted)  # Ouput => Elzero-Academy

# Change To Lower Case
last_result = joined.lower()  # Ouput => elzero-academy

print(last_result)

print('#'*25)

my_string = "Elzero Academy"
print("-".join(my_string.split(" ")).lower())

print('#'*25)

my_string = "Elzero Academy"
print(my_string.replace(" ", "-").lower())
