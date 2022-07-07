def substringCount(string):
    '''
    to find how many substrings there in string
    '''
    substringCounter = 0
    l = string.split()
    for element in l:
        counter = 0
        for i in element:
            counter += 1
        if counter > 0:
            substringCounter += 1
    print("There are {} substrings".format(substringCounter))


string = "I Love Elzero Web School"
substringCount(string)


def findSubstringCounter(string, substing):
    '''
    to find a certain substtring
     among the string
    '''
    substing = substing.lower()
    counter = 0
    for letter in string:
        if letter == substing:
            counter += 1
    return counter


string = "I Love Elzero Web School"
print(findSubstringCounter(string, 'O'))


def find_substring_counter(string, substing):
    '''
    to find a certain substtring
     among the string with count function
    '''
    substing = substing.lower()
    print(string.count(substing))


string = "I Love Elzero Web School"
find_substring_counter(string, 'o')


print('#'*50)


def count_substring(string, sub_string):

    thecount = 0

    for index in range(len(string)):

        if string[index:].startswith(sub_string):

            thecount += 1

    return thecount


print(count_substring("I Love Elzero Web School", "o"))  # 4
