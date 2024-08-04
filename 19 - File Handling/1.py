# https://github.com/Asabeneh/30-Days-Of-Python/blob/master/19_Day_File_handling/19_file_handling.md
# Syntax
# open('filename', mode) # mode(r, a, w, x, t,b)  could be to read, write, update

'''
    "r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
    "a" - Append - Opens a file for appending, creates the file if it does not exist
    "w" - Write - Opens a file for writing, creates the file if it does not exist
    "x" - Create - Creates the specified file, returns an error if the file exists
    "t" - Text - Default value. Text mode
    "b" - Binary - Binary mode (e.g. images)
'''
f = open('19 - File Handling/sample.txt')
print(f) # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'>
txt = f.read() #can specify n number of characters to be printed 'f.read(10)'
print(type(txt))
print(txt) # the actual content
print("\n")
line = f.readline()
#print(type(line))
print(line)

'''
print("\n")
lines = f.readlines()
print(type(lines))
print(lines)
print("\n")
lines = f.read().splitlines()
print(type(lines))
print(lines)

'''



f.close()