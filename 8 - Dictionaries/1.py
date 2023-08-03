#https://github.com/Asabeneh/30-Days-Of-Python/blob/master/08_Day_Dictionaries/08_dictionaries.md

#A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.

"""
Create an empty dictionary called dog
Add name, color, breed, legs, age to the dog dictionary
Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
Get the length of the student dictionary
Get the value of skills and check the data type, it should be a list
Modify the skills values by adding one or two skills
Get the dictionary keys as a list
Get the dictionary values as a list
Change the dictionary to a list of tuples using items() method
Delete one of the items in the dictionary
Delete one of the dictionaries
"""

#Create an empty dictionary called dog
dog = {'key':'value'} #dictionary syntax

dog = {} #empty dictionary

#Add name, color, breed, legs, age to the dog dictionary
dog = {'name':'Malcolm',
'color':'brown',
'breed':'boxer',
'legs':'strong',
'age':'1',
}

#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
'first_name':'Brandon', 
'last_name':'Ramirez', 
'gender':'Male', 
'age':'22', 
'marital-status':'Single', 
'skills':['JavaScript', 'React', 'Node', 'Java', 'Python'],
'country':'USA', 
'city':'Texas City',
'address':'123 Lone Star Street'
}

#Get the length of the student dictionary
dct_len = len(student)
print(dct_len) #9 items

print(student['first_name']) #prints value of key 'first_name'
print(student.get('first_name')) #prints value of key 'first_name'
print(student['skills'][0]) #prints first element in 'skills' key array
print(student['gpa']) #'Error'
print(student.get('gpa')) #'None'

#Get the value of skills and check the data type, it should be a list
n = 3
print(type(student['skills']))
print(type(student['skills'][n]))

# syntax to add key/value pair
worker = {'fname':'John', 'lname':'Doe', 'experience':'2yrs', 'salary':'10$'}
dct['dept'] = 'r&d'	#creates a new key/value pair entry into dictionary

#Modify the skills values by adding one or two skills
student['skills'].append('HTML')
student['skills'].append('CSS')

# syntax to modify item
company = {'industry':'AI', 'name':'OpenAI', 'stock':'50,000', 'age':'5yrs'}
company['stock'] = '38,547'


#Get the dictionary keys as a list
keys = student.keys()
print(keys)     # student_keys(['key1', 'key2', 'key3', 'key4'])
#Get the dictionary values as a list
values = student.values()
print(values)   # student_values(['key1', 'key2', 'key3', 'key4'])

#Change the dictionary to a list of tuples using items() method
# syntax to change the dictionary to tuples
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])
#Delete one of the items in the dictionary

# syntax to 'clear' or reset a dictionary
print(dog.clear()) # None

# syntax to copy dictionary into another
student_copy = student.copy()

#Delete one of the dictionaries
del student

print(student_copy)