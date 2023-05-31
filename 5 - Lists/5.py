import math 
# Declare an empty list
empty_list = [] # this is an empty list, no item in the list
print(len(empty_list)) # 0
# Declare a list with more than 5 items
list = [2,4,8,16,32,64]
# Find the length of your list
print(len(list))
# Get the first item, the middle item and the last item of the list
print(list[0])
print(list[len(list) - 1])
# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Brandon", 22, "5'6in", "single", "425 Beech Street"]
# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle",  "Amazon"]
# Print the list using print()
print(it_companies);
# Print the number of companies in the list
print(len(it_companies))
# Print the first, middle and last company
print(it_companies[0])
print(it_companies[int(len(it_companies) / 2)])
print(it_companies[len(it_companies) - 1])

# Print the list after modifying one of the companies
it_companies[0] = "Uber"
# Add an IT company to it_companies
it_companies.append("Ebay")
# Insert an IT company in the middle of the companies list
it_companies.insert(int(len(it_companies) / 2), "Robinhood")
# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[4] = "Tesla"
it_companies[6] = it_companies[6].upper();
print(it_companies);
# Join the it_companies with a string '#;  '
new_it = it_companies.copy();
# Check if a certain company exists in the it_companies list.
print(it_companies.count("Facebook"))
# Sort the list using sort() method
it_companies.sort();
# Reverse the list in descending order using reverse() method
it_companies.reverse();
# Slice out the first 3 companies from the list
print(new_it[4:]);
# Slice out the last 3 companies from the list
new_it.pop();
new_it.pop();
new_it.pop();
# Slice out the middle IT company or companies from the list
del it_companies[int(len(it_companies) / 2)];
# Remove the first IT company from the list
del new_it[0];
# Remove all IT companies from the list
new_it.clear();
# Destroy the IT companies list

# Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

tech_stack = front_end + back_end;
#     After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = tech_stack.copy();
full_stack.insert(tech_stack.index('Redux') + 1, 'Python');
full_stack.insert(tech_stack.index('Redux') + 2, 'SQL');
print(full_stack);
# Exercises: Level 2

#     The following is a list of 10 students ages:

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#     Sort the list and find the min and max age
ages.sort()
#     Add the min age and the max age again to the list
ages.append(ages.index(min(ages)) + ages.index(max(ages)))
#     Find the median age (one middle item or two middle items divided by two)
ages.insert(int(len(ages) / 2), ages[int(len(ages) / 2)])
#     Find the average age (sum of all items divided by their number )

#     Find the range of the ages (max minus min)
range = max(ages) - min(ages);
print(range)

#     Compare the value of (min - average) and (max - average), use abs() method

#     Find the middle country(ies) in the countries list

#     Divide the countries list into two equal lists if it is even if not one more country for the first half.

#     ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
