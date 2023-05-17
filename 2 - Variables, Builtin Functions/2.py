"""
Exercises: Level 2

    Check the data type of all your variables using type() built-in function
    Using the len() built-in function, find the length of your first name
    Compare the length of your first name and your last name
    Declare 5 as num_one and 4 as num_two
        Add num_one and num_two and assign the value to a variable total
        Subtract num_two from num_one and assign the value to a variable diff
        Multiply num_two and num_one and assign the value to a variable product
        Divide num_one by num_two and assign the value to a variable division
        Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
        Calculate num_one to the power of num_two and assign the value to a variable exp
        Find floor division of num_one by num_two and assign the value to a variable floor_division
    The radius of a circle is 30 meters.
        Calculate the area of a circle and assign the value to a variable name of area_of_circle
        Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
        Take radius as user input and calculate the area.
    Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
    Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
"""

fname = "Brandon";
lname = "Schwartz";

if len(fname) > len(lname):
    print("The length of the first name is greater than the length of the last name.")
else:
    print("The length of the first name is less than the length of the last name.")

num_one = 5;
num_two = 4;
total = num_one + num_two;
dif = num_one - num_two;
product = num_one * num_two;
division = num_one / num_two;
remainder = num_one % num_two;
exp = num_one ** num_two;
floor_division = num_one // num_two;
area_of_circle = 3.14 * 30 ** 2;
circum_of_circle = 2 * 3.14 * 30;

country = "";
age = 0;
print("Enter your first name:")
fname = input()
print("Enter your last name:")
lname = input()
print("Enter your country of origin:")
country = input()
print("Enter your age:")
age = input()


print(f"Your first name: {fname}, last name: {lname}, country: {country}, age: {age}.")
print(f"The length of your first name is {len(fname)}.")
print(f"The length of your last name is {len(lname)}.")








