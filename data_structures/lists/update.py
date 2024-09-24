# create a list of vowels
#https://www.programiz.com/python-programming/methods/list/insert
vowel = ['a', 'e', 'i', 'u']

# 'o' is inserted at index 3 (4th position)
print(vowel)
'''
Here, elem is inserted to the list at the ith index. All the elements after elem are shifted to the right.
'''
vowel.insert(3, 'o')

print('List:', vowel)

# Output: List: ['a', 'e', 'i', 'o', 'u']


#deletion of the elements with value specified
# create a list
prime_numbers = [2, 3, 5, 7, 9, 11]

# remove 9 from the list
prime_numbers.remove(9)
prime_numbers.pop()
prime_numbers.pop(2)

'''
    syntax: list_name.pop(index)
    index (optional) – The value at the index is popped out and removed. If the index is not given, then the last element is popped out and removed.
'''


# Updated prime_numbers List
print('Updated List: ', prime_numbers)
# remove all elements
prime_numbers.clear()
print('Empty list: ', prime_numbers)
# Output: Updated List:  [2, 3, 7]