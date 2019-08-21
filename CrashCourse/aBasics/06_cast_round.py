#%% displayHelper
from CrashCourse.displayhelper import *

#%% Cast -> int()
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
describe(x)
describe(y)
describe(z)

#%% Cast -> float()
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
describe(x)
describe(y)
describe(z)
describe(w)

#%% Cast -> str()
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
describe(x)
describe(y)
describe(z)

#%% sequence
list = [1,2,3,3]
complexList = [[1, "A"], [2, "B"]]
describe(set(list))
describe(tuple(list))
describe(tuple(set(list)))
describe(dict(complexList))

#%% round()
print(round(10))
print(round(10.7))
print(round(5.5))
print(round(2.665, 2))
print(round(2.675, 2))
