try:
    print(10 + '5')
except:
    print('Something went wrong')

try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2024 - int(year_born)
    print('You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occur')
except ValueError:
    print('Value error occur')
except ZeroDivisionError:
    print('zero division error occur')
else:
    print('I usually run with the try block')
finally:
    print('I alway run.')