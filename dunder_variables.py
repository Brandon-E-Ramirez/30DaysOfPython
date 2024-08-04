# https://www.pythonmorsels.com/dunder-variables/
import math
print(math.sqrt.__doc__)

def what(thing):
    print("That's a", type(thing).__name__)

what("[1,2]")
what([1,2])

#* initializer or constructor in python
# https://www.pythonmorsels.com/what-is-init/
