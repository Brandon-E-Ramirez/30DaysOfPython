import cmath;
"""
Exercises: Level 1

"""

    #Declare a function add_two_numbers. It takes two parameters and it returns a sum.
import math;
def add_two_numbers (a, b):
    sum = a + b;
    return sum;
    #Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
funcArea = add_two_numbers(1,9);
print(f"{funcArea} \n");

def circleArea (radius):
    area = radius * radius * math.pi ;
    return area;
print(circleArea(3));
print("\n")
    #Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums (*args):
    sum = 0;
    for num in args:
        sum += num;
    return sum
add = add_all_nums(2,4,1,5,6,0);
print(f"The sum of all numbers is: {add}\n");
    #Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
inputTemp = 20;
def CelciusToFahrenheit (Celcius):
    Fahrenheit=((9/5)*Celcius)+32;
    return Fahrenheit;
print(f"{inputTemp} degrees Celcius is {CelciusToFahrenheit(inputTemp)} degrees in Fahrenheit\n")
    #Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
seasons = ["January","February","March","April","May","June","July","August","September","October","Novemeber","December"];
def season (month):
    if month =='January' or month == 'February' or month == 'March':
        return "Spring";
    elif month == 'April' or month=='May'or month== 'June':
        return "Summer";
    elif month == 'July'or month=='August' or month== 'September':
        return "Autumn";
    elif month == 'October' or month=='November' or month== 'Decemberr':
        return "Winter";
    else: 
        print("Invalid Month!");

print(f"The month {seasons[5]} is in the season of {season(seasons[5])}\n");

    #Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a,b,c):
    #solve ax^2 + bx +c = 0
    ans = "";
    ansPlus= ((-b) + cmath.sqrt((b**2)-(4*a*c)))/2*(a);
    ansMinus= ((-b) - cmath.sqrt((b**2)-(4*a*c)))/2*(a);
    ans = str(ansPlus) + ", " + str(ansMinus);
    return ans;

x=3;
y=4;
z=2;

res = solve_quadratic_eqn(x,y,z);
print(f"The quadratic equations solutions \"x\" (in the expression \"ax^2 + bx + c 0\") for a={x}, b={y}, & c={z} is: {res}\n")

    #Write a function called calculate_slope which return the slope of a linear equation
    #y = mx +b
    #Standard form Ax + By = C

#first vertex (a,b), second is (c,d) (in the form "(x,y)")
#use formula (d-b)/(c-a) or "rise over run"
def calculate_slope(a,b,c,d):
        slope = (d-b)/(c-a);
        return slope;
a = 2
b = 6
c = 5
d = 10
print(f"The slope of a={a}, b={b}, c={c}, & d={d} is {calculate_slope(a,b,c,d)}")

    #Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(list):
    for i in list:
        print(i,end=" ")
    print("\n")

arr = ["Texas","Alabama", "New York", "Utah", "Washington"]
print_list(arr);
    #Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(arr):
        for i in range(len(arr) - 1, -1, -1):
            print(arr[i], end=" ");

reverse_list(arr);




"""
print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list1(["A", "B", "C"]))
# ["C", "B", "A"]

    Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
    Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))      [2, 3, 7, 9, 5]

    Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9];
print(remove_item(numbers, 3))  # [2, 7, 9]

    Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.

print(sum_of_numbers(5))  # 15
print(sum_all_numbers(10)) # 55
print(sum_all_numbers(100)) # 5050

    Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
    Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
"""