# #https://github.com/Asabeneh/30-Days-Of-Python/blob/master/04_Day_Strings/04_strings.md
# # Strings only
# first_name = 'Asabeneh'
# last_name = 'Yetayeh'
# language = 'Python'
# formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
# print(formated_string)

# # Strings  and numbers
# radius = 10
# pi = 3.14
# area = pi * radius ** 2
# formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area) # 2 refers the 2 significant digits after the point
# print(formated_string);
# python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
# formated_string = 'The following are python libraries:%s' % (python_libraries)
# print(formated_string) # "The following are python libraries:['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']"

# greeting = 'Hello, World!'
# print(greeting[::-1]) # !dlroW ,olleHa


#  Exercises - Day 4

#     Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
#     Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
#     Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding for All"
#     Print the variable company using print().
print(company)
#     Print the length of the company string using len() method and print().
print(len(company))
#     Change all the characters to uppercase letters using upper() method.
print(company.upper());
#     Change all the characters to lowercase letters using lower() method.
print(company.lower())
#     Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize());
print(company.title());
print(company.swapcase())
#     Cut(slice) out the first word of Coding For All string.
print(company[7:])
#     Check if Coding For All string contains a word Coding using the method index, find or other methods.
if 'Coding' in company:
    print("Found!")
else:
    print("Not found!")

#     Replace the word coding in the string 'Coding For All' to Python.
print(company.replace("Coding","Python"))

#     Change Python for Everyone to Python for All using the replace method or other methods.

#     Split the string 'Coding For All' using space as the separator (split()) .
print(company.split(" "));
#     "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(', '));
#     What is the character at index 0 in the string Coding For All.
print(company[0])
#     What is the last index of the string Coding For All.
print(company[len(company) - 1])
#     What character is at index 10 in "Coding For All" string.
#     Create an acronym or an abbreviation for the name 'Python For Everyone'.
abbr = 'PFE'
#     Create an acronym or an abbreviation for the name 'Coding For All'.
acr = 'CFA'
#     Use index to determine the position of the first occurrence of C in Coding For All.
print(company.find("C"))
#     Use index to determine the position of the first occurrence of F in Coding For All.
#     Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(company.rfind('l'))
#     Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find("because"))
#     Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rfind("because"))
#     Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence[31:54])
#     Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

#     Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

#     Does ''Coding For All' start with a substring Coding?

#     Does 'Coding For All' end with a substring coding?

#     '   Coding For All      '  , remove the left and right trailing spaces in the given string.

#     Which one of the following variables return True when we use the method isidentifier():

#         30DaysOfPython
#         thirty_days_of_python = True
#     The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.


#     Use the new line escape sequence to separate the following sentences.
#     I am enjoying this challenge.
#     I just wonder what is next.

# Use a tab escape sequence to write the following lines.
str1 = 'Name\tAge\tCountry\tCity\t\nBrandon\t22\tAmerica\tLa Marque\n'
print(str1)
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki

#     Use the string formatting method to display the following:

radius = 10
area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
print("The area of a circle with %d is %.2f."%(radius, area))



#     Make the following using string formatting methods:

# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144