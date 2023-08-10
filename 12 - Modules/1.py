import helper
import random
import string

fullName = helper.generate_full_name("Brandon","Ramirez");
print(f"Full name is: {fullName}")

#https://github.com/Asabeneh/30-Days-Of-Python/blob/master/12_Day_Modules/12_modules.md

#Writ a function which generates a six digit/character random_user_id.

def random_usr_id():
    length = 6  # length of the random user ID
    alph = list(string.ascii_lowercase)
    char = ['!', '@', '#', '$', '%', '^', '*', "(", ')', '-', '+', '=']
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    arr = []  # This arr will hold the usr_id
    for x in range(0, length):
        choice = random.randint(0, 2)  # Used to choose if the next element appended to the id array will be from alph, char, or num
        if choice == 0:  # Choose a letter from the alphabet
            i = random.randint(0, len(alph) - 1)
            arr.append(str(alph[i]))
        elif choice == 1:  # Use a character
            j = random.randint(0, len(char) - 1)
            arr.append(str(char[j]))
        elif choice == 2:  # Use a number
            k = random.randint(0, len(num) - 1)
            arr.append(str(num[k]))
        else:
            print('Error in \'random_usr_id\' logic!')
    return ''.join(arr)

print("Randomly generated user id:")
print(random_usr_id())


"""
Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but 
it takes two inputs using input(). One of the inputs is the number of characters and the second input is the 
number of IDs which are supposed to be generated.
"""

idsGenerated, idSize = input('Enter the number of ids that will be generated and sizes (\" \" between inputs):').split()

def generate_id(size, count):
    length = int(size)  # length of the random user ID
    lists = lists = [[] for _ in range(int(count))]
    
    alph = list(string.ascii_lowercase)
    char = ['!', '@', '#', '$', '%', '^', '*', "(", ')', '-', '+', '=']
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    
    for b in range(0, int(count)):
      arr = []  # This arr will hold the usr_id
      for x in range(0, length):
        choice = random.randint(0, 2)  # Used to choose if the next element appended to the id array will be from alph, char, or num
        if choice == 0:  # Choose a letter from the alphabet
            i = random.randint(0, len(alph) - 1)
            arr.append(str(alph[i]))
        elif choice == 1:  # Use a character
            j = random.randint(0, len(char) - 1)
            arr.append(str(char[j]))
        elif choice == 2:  # Use a number
            k = random.randint(0, len(num) - 1)
            arr.append(str(num[k]))
        else:
            print('Error in \'random_usr_id\' logic!')
      lists[b] = arr
    return lists

print(generate_id(idSize, idsGenerated))

#Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).

def rgb_color_gen():
  rgb_code = [[],[],[]]
  limit = 256
  for x in range(0,3):
    rgb_code[x].append((random.randint(0,limit)))
  return rgb_code

print(f"Randomly generated rgb code: {rgb_color_gen()}")