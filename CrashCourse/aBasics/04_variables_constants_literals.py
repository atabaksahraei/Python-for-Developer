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
import CrashCourse.aBasics.constant as constant
# import constant
print(constant.PI)
print(constant.GRAVITY)


#%% multiline
mystr = """
            ABC
            Hi

        """
print(mystr)

#%% Literals
# Numeric
a = 0b1010 #Binary
b = 100 #Decimal
c = 0o310 #Octal
d = 0x12c #Hexadecimal

#Float
float_1 = 10.5 
float_2 = 1.5e2

#Complex 
x = 3.14j
x_imag= x.imag
x_real= x.real

# string
strings = "This is a String"
char = "C"
multiline_str = """This is a
 multiline string
 with more than
 one
 line
 code."""
unicode = u"\u0053\u0044\u0058\u002d\u0041\u0047"
raw_str = r"raw \n string" # -> in c#: @"raw \n string"
