#%% displayHelper
%cd ".."
from displayhelper import *

#%% Numbers
number = 5
describe(number)

double = 1.2
describe(double)

complex = 1+2j
describe(complex)
describe(complex.imag)
describe(complex.real)

#%% Strings
str = "SDX-AG"
str_2 = 'SDX-AG'
describe(str)
describe(str_2)

str_multiline = """SDX-AG
eXperts"""
describe(str_multiline)

describe(str[0:3])

#%% strings is a immutable (unchangeable object) char array
str = "SDX-AG"
str[0] = "A" # error!

#%% List
# List is an ordered sequence of items.
list = [1, 2, 3]
describe(list)
describe(list[0])

#%% Tuple
# Tuple is an ordered sequence of items same as list.
# Difference to list: tuples are immutable.
tuple = (1, "SDX-AG", 1+3j, 10e-3)
describe(tuple[0])
tuple[0] = 2 # Error!
describe(tuple)

#%% Set
# Set is an unordered collection of unique items.
set = { 5, 2, 3, 1, 4}
describe(set)

#%% Dictionary
# Dictionary is an unordered collection of unique items same as set.
# Difference to set: list of key-value pairs.
dict = {"key1":"value1",2:"value2", "key3":False}
describe(dict)

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

# %%
