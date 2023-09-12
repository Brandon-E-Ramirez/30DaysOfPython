"""
## 💻 Exercises: Day 13

1. Filter only negative and zero in the list using list comprehension
   ```py
   ```
"""
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
pos = [i for i in numbers if i >= 0]
print(pos)

"""
2. Flatten the following list of lists of lists to a one dimensional list :

   ```py
   list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

   output
   [1, 2, 3, 4, 5, 6, 7, 8, 9]
   ```
"""

   
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list = [ number for row in list_of_lists for number in row]
print(list)


print("part 3")
"""
3. Using list comprehension create the following list of tuples:
   ```py
   [(0, 1, 0, 0, 0, 0, 0),
   (1, 1, 1, 1, 1, 1, 1),
   (2, 1, 2, 4, 8, 16, 32),
   (3, 1, 3, 9, 27, 81, 243),
   (4, 1, 4, 16, 64, 256, 1024),
   (5, 1, 5, 25, 125, 625, 3125),
   (6, 1, 6, 36, 216, 1296, 7776),
   (7, 1, 7, 49, 343, 2401, 16807),
   (8, 1, 8, 64, 512, 4096, 32768),
   (9, 1, 9, 81, 729, 6561, 59049),
   (10, 1, 10, 100, 1000, 10000, 100000)]
   ```

   """

arrOne = [0 if i != 1 else 1 for i in range(7)]
print(arrOne)
arrTwo = [1 for i in range(8)]
print(arrTwo)
arrThree = [(i-1)*2 if i >= 1 else 2 for i in range(8)]
print(arrThree)
arrFour = [3 if i == 0 else 3**i for i in range(8)]
print(arrFour)
arrFive = [4 if i == 0 else 4**i for i in range(8)]
print(arrFive)

"""
4. Flatten the following list to a new list:
   ```py
   countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
   output:
   [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
   ```
   """

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]


"""
5. Change the following list to a list of dictionaries:
   ```py
   countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
   output:
   [{'country': 'FINLAND', 'city': 'HELSINKI'},
   {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
   {'country': 'NORWAY', 'city': 'OSLO'}]
   ```


   """


"""
6. Change the following list of lists to a list of concatenated strings:
   ```py
   names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
   output
   ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
   ```

"""

"""
7. Write a lambda function which can solve a slope or y-intercept of linear functions.
"""