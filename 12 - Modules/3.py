import random
"""

    Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
    Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.

"""

def shuffle_list(arr):
    new_arr = random.sample(arr, len(arr));
    return new_arr;

arr = [1,2,3,4,5,6,7,8,9,0]
print("This is the shuffled list: ", shuffle_list(arr))


o = input("Enter length of randomly generated list consisting of 0-9: ")
def randNums(amnt):
    amnt = int(amnt)
    arr = []
    for i in range (amnt) :
        arr.append(random.randint(0,9))
    return arr;
print(f"Your list is: {randNums(o)}")