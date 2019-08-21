#%% displayHelper
from CrashCourse.displayhelper import *

#%% Variables
website = "sdx-ag.de"
print(website)

# multiple
a, b, c = 5, 3.2, "Hello"

# w = "same" + str(a)
# x = y = z = "same" + str(a)

w = "same"
x = y = z = "same"

display_ref(w)
display_ref(x)
display_ref(y)
display_ref(z)

#%% Call by Reference
l=[8, 11]
display_ref(l)

l[0] = 10
display_ref(l)

l.append(12)
display_ref(l)

def doStuff(list):
    display_ref(l)

doStuff(l)

# https://www.python-course.eu/passing_arguments.php

#%% Constants (Not Recommended)
# Create a constant.py
import CrashCourse.aBasics.constant as constant
# import constant
print(constant.PI)
constant.PI = 100
print(constant.PI)
print(constant.GRAVITY)

from CrashCourse.aBasics.constant import *
print(PI)
PI = 100
print(PI)
print(GRAVITY)

