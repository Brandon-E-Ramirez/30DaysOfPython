#https://github.com/Asabeneh/30-Days-Of-Python/blob/master/02_Day_Variables_builtin_functions/02_variables_builtin_functions.md
#*help('keywords') gives you a list of all the python keywords
#*help ('keyword') gives you more details about a specific keyword
#*use: exit() to exit the python CL mode
#*Some of the most commonly used Python built-in functions are the following: print(), len(), type(), int(), float(), str(), input(), list(), dict(), min(), max(), sum(), sorted(), open(), file(), help(), and dir().
#how to find fibonacci sequence in python? #*code made using blackbox extension 

def fib(n):
  a = 0
  b = 1
  while b<n:
    print(b) 
    temp = a
    a = b
    b = temp+b
fib(4)

"""
Exercises: Level 1

    Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
    Write a python comment saying 'Day 2: 30 Days of python programming'
    Declare a first name variable and assign a value to it
    Declare a last name variable and assign a value to it
    Declare a full name variable and assign a value to it
    Declare a country variable and assign a value to it
    Declare a city variable and assign a value to it
    Declare an age variable and assign a value to it
    Declare a year variable and assign a value to it
    Declare a variable is_married and assign a value to it
    Declare a variable is_true and assign a value to it
    Declare a variable is_light_on and assign a value to it
    Declare multiple variable on one line

"""

#Source: https://stackoverflow.com/questions/36360381



















