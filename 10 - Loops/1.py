"""Exercises: Level 1
    Iterate 0 to 10 using for loop, do the same using while loop.
    Iterate 10 to 0 using for loop, do the same using while loop.
"""
#Iterate 0 to 10 using for loop, do the same using while loop.
count = 11;
for num in range(0,count):
	print(num);

print('\n');
base = 0;
while (base < count):
	print(base);
	base = base + 1;
else:
	print(f"Terminated, {count} items printed");

#Iterate 10 to 0 using for loop, do the same using while loop.
count = 10;
for num in range(count, -1, -1):
	print(num);

print('\n');
base = 0;
cnt = 0;
while (count >= base):
	print(count)
	count = count - 1
	cnt += 1
else:
	print(f"\nTerminated, {cnt} items printed...");
"""
    Write a loop that makes seven calls to print(), so we get on the output the following triangle:

      #
      ##
      ###
      ####
      #####
      ######
      #######
"""
#update number of '*' in the string every time the row increases

limit = 7;
c = '*';
for x in range(0, limit):
    for y in range(0, x + 1):
	    # 'end=""' is used when we do not want a new line
        #we can keep printing on the same line indefinititely
        print(f"{c}",end="");
    print("\r");

"""
Use nested loops to create the following:
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
"""
character = "# ";
lim = 8;
for u in range(0,lim):
	for v in range(0,lim):
		print(f"{character}",end="")
	print("\r");

"""
Print the following pattern:
0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
"""
upper = 10;
for o in range(0,upper + 1):
    calc = o ** 2;
    print(f"{o} x {o} = {calc}");
"""
    Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
    Use for loop to iterate from 0 to 100 and print only even numbers
    Use for loop to iterate from 0 to 100 and print only odd numbers
"""

arr = ['Python', 'Numpy','Pandas','Django', 'Flask'] 
for i in arr :
	print(i, end=" ");

max = 100;
for i in range(0,max+1):
    if (i % 2 == 0):
        print(f"Even: {i}\n");
    elif i % 2 != 0:
        print(f"Odd:{i}\n")

"""
Exercises: Level 2
    Use for loop to iterate from 0 to 100 and print the sum of all numbers.
The sum of all numbers is 5050.
Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
The sum of all evens is 2550. And the sum of all odds is 2500.
"""
 
sum = 0;
maxima = 100;
for k in range(0,maxima+1):
    print(f"Current sum = {sum}, ",end="");
    sum += k;
    print(f"Updated sum = {sum}\n",end="");
print(f"\nThe sum of 0 to 100 is: {sum}\n");

max = 100;
sumEven = 0;
sumOdds=  0;
for i in range(0,max+1):
    if (i % 2 == 0):
        print(f"Even: {i} ");
        print(f"Current sum is = {sumEven}, ",end="")
        sumEven += i;
        print(f"Updated sum = {sumEven}\n")
    elif i % 2 != 0:
        print(f"Odd:{i} ")
        print(f"Current sum is = {sumOdds}, ",end="")
        sumOdds += i;
        print(f"Updated sum = {sumOdds}\n")

print(f"\nThe sum of evens is: {sumEven}\n");
print(f"The sum of odds is: {sumOdds}\n");

"""
Exercises: Level 3

    Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
    This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
    Go to the data folder and use the countries_data.py file.
        What are the total number of languages in the data
        Find the ten most spoken languages from the data
        Find the 10 most populated countries in the world
"""


