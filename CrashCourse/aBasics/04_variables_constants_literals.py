#%% Variables
website = "sdx-ag.de"
print(website)

# multiple
a, b, c = 5, 3.2, "Hello"

x = y = z = "same"
print (x)
print (y)
print (z)
print(id(x))
print(id(y))
print(id(z))

#%% Call by Reference
def doStuff(list):
    print(id(list))
   
l=[10, 11]
print(id(x))
l.append(20)
print(id(l))
doStuff(l)

# https://www.python-course.eu/passing_arguments.php

#%% Constants
# Create a constant.py in a module
import Basics.aBasics.constant as constant
# import constant
print(constant.PI)
print(constant.GRAVITY)


#%% multiline
mystr = """
            ABC
            Hi

        """
print(mystr)

