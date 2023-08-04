"""Exercises: Level 1
    Iterate 0 to 10 using for loop, do the same using while loop.
    Iterate 10 to 0 using for loop, do the same using while loop.
    Write a loop that makes seven calls to print(), so we get on the output the following triangle:

      #
      ##
      ###
      ####
      #####
      ######
      #######

char c = '*';
for x in range():


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
rows = 8;
columns = 8;
char = '#';

"""
for(x in rows):
	for(y in columns):
		print(char);
"""

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









    Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

    Use for loop to iterate from 0 to 100 and print only even numbers

    Use for loop to iterate from 0 to 100 and print only odd numbers
"""




"""
Exercises: Level 2

    Use for loop to iterate from 0 to 100 and print the sum of all numbers.

The sum of all numbers is 5050.

Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

The sum of all evens is 2550. And the sum of all odds is 2500.
"""






"""
Exercises: Level 3

    Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
    This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
    Go to the data folder and use the countries_data.py file.
        What are the total number of languages in the data
        Find the ten most spoken languages from the data
        Find the 10 most populated countries in the world
"""