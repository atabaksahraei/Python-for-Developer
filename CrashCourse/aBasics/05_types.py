#%% displayHelper
from CrashCourse.displayhelper import *

#%% Numbers
number = 5
describe(number)

double = 1.2
describe(double)

complex = 1+2j
describe(complex)
describe(complex.imag)
describe(complex.real)

#%% List
# List is an ordered sequence of items.
list = [1, 2, 3]
describe(list)
describe(list[0])

#%% Tuple
# Tuple is an ordered sequence of items same as list.
# Difference to list: tuples are immutable.
tuple = (1, "SDX-AG", 1+3j, 10e-3)
describe(tuple)

#%% Strings
str = "SDX-AG"
str_2 = 'SDX-AG'
describe(str)
describe(str_2)

str_multiline = """SDX-AG
eXperts"""
describe(str_multiline)

describe(str[0:3])

# strings are immutable
# str[0] = "A" # Generates error

#%% Set
# Set is an unordered collection of unique items.
set = { 5, 2, 3, 1, 4}
describe(set)

#%% Dictionary
# Dictionary is an unordered collection of key-value pairs.
dict = {"key1":"value1",2:"value2", "key3":False}
describe(dict)

