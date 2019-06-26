#%% displayHelper
from CrashCourse.displayhelper import *

#%% if
if condition:
    statement()

#%% if else
if condition:
    statement("A")
else:
    statement("B")


if condition: statement("C")
else: statement("D")


#%% if elseif
condition_2 = True

if condition:
    statement("A")
elif condition_2:
    statement("B")
else:
    statement()
