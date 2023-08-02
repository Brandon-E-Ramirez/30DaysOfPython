#https://github.com/Asabeneh/30-Days-Of-Python/blob/master/07_Day_Sets/07_sets.md

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


"""
Exercises: Level 1

    Find the length of the set it_companies
    Add 'Twitter' to it_companies
    Insert multiple IT companies at once to the set it_companies
    Remove one of the companies from the set it_companies
    What is the difference between remove and discard
"""
length = len(it_companies);
print(length);

it_companies.add('Twitter');
print(it_companies);

it_companies.update(['Threads', 'X', 'Uber', 'Brother']);
print(it_companies);

it_companies.remove('Brother');
print(it_companies);

#"discard()" will not give you an error if the item does not exist, but remove() will.



"""
Exercises: Level 2

    Join A and B
    Find A intersection B
    Is A subset of B
    Are A and B disjoint sets
    Join A with B and B with A
    What is the symmetric difference between A and B
    Delete the sets completely
"""

"""
Exercises: Level 3

    Convert the ages to a set and compare the length of the list and the set, which one is bigger?
    Explain the difference between the following data types: string, list, tuple and set
    I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.



"""






