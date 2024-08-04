#https://github.com/Asabeneh/30-Days-Of-Python
import math
print('Hello world!')
# Day 1 - 30DaysOfPython Challenge

print(2 + 3)             # addition(+)
print(3 - 1)             # subtraction(-)
print(2 * 3)             # multiplication(*)
print(3 / 2)             # division(/)
print(3 ** 2)            # exponential(**)
print(3 % 2)             # modulus(%)
print(3 // 2)            # Floor division operator(//)

# Checking data types
print(type(10))          # Int
print(type(3.14))        # Float
print(type(1 + 3j))      # Complex number
print(type('Asabeneh'))  # String
print(type([1, 2, 3]))   # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple




"""
computer Exercises - Day 1
Exercise: Level 1

    Check the python version you are using
    Open the python interactive shell and do the following operations. The operands are 3 and 4.
        addition(+)
        subtraction(-)
        multiplication(*)
        modulus(%)
        division(/)
        exponential(**)
        floor division operator(//)
"""
#!Code starts here
#*Highlighted info
#?Questions
#TODO Things that need to be done

#* python --version
print(3 * 4)
print(3 - 4)
print(3 + 4)
print(3 % 4)
print(3 / 4)
print(3 ** 4)
print(3 // 4)
"""
    Write strings on the python interactive shell. The strings are the following:
        Your name
        Your family name
        Your country
        I am enjoying 30 days of python
    Check the data types of the following data:
        10
        9.8
        3.14
        4 - 4j
        ['Asabeneh', 'Python', 'Finland']
        Your name
        Your family name
        Your country

Exercise: Level 2

    Create a folder named day_1 inside 30DaysOfPython folder. Inside day_1 folder, create a python file helloworld.py and repeat questions 1, 2, 3 and 4. Remember to use print() when you are working on a python file. Navigate to the directory where you have saved your file, and run it.
"""


"""
Exercise: Level 3

    Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
    Find an Euclidian distance between (2, 3) and (10, 8)
"""
#* Different data types in Python: 

num = 1
float = 3.14
complex = 3 - 2j
str = 'Python is easy'
bool = True
"""

    *List is a collection which is ordered and changeable. Allows duplicate members.
    *Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    *Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
    *Dictionary is a collection which is ordered** and changeable. No duplicate members.

"""
list = [1, 2, 3, 4, 5, 2, 6, 7,0] #can grown, shrink. Ordered list
tuple = (1,2,3,4,5,3,6,7,8,9,0) #immutable, ordered 

set = {"apple", "banana", "cherry", True, 1, 2}#duplicates ignoreda

list.sort()
print(list)
print(tuple)
print(set)

#*Dictionary in Python
{
'fname':'Brandon',
'lname': 'Ramirez',
'age':22,
'major': 'CS',
'undergrad?':True
}





#*Find euclidean distance between two points: d = sqrt((x2 - x1)^2 + (y2 - y1)^2)
p1 = [2,3]
p2 = [10,8]

def euclideanDist():
    dist = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
    print(dist)

euclideanDist()