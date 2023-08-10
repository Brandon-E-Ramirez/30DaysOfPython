import random
import modulesOne as mod_one
import string
"""
    Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
    Write a function generate_colors which can generate any number of hexa or rgb colors.

   generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
   generate_colors('hexa', 1) # ['#b334ef']
   generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
   generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
"""
    #Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array 
    #(six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 
    # 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).


def hexa_color(type):
    numSystem = str(type)
    hexLetters = ["a", "b", "c", 'd', 'e', 'f']
    #hexDigits = string.digits
    sharp = '#'
    size = 6
    arrValues = ""

    match numSystem:
        case ("hex"):
            for a in range(0, size):
                numOrLetter = random.randint(0,1)
                if(numOrLetter == 0):
                    arrValues += str(random.randint(0,9))
                elif(numOrLetter == 1):
                    arrValues += str(hexLetters[random.randint(0,5)])
            return str(sharp + arrValues)
        case ("rgb"):
            return str(mod_one.rgb_color_gen())
        case _:
            return "There was an error with your input, please enter a valid number system (\"hex\", \"rgb\")"

x = input("Input \"hex\" or \"rgb\" to get a randomly generated color: ")
output = hexa_color(x)
print(f"\"{x}\" yields: {output}");

