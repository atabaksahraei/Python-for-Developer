#%% displayHelper
from CrashCourse.displayhelper import *

#%% foreach
for var in sequence:
    statement(var)

#%% for
for i in range(0, 5):
    statement(var)

#%% for/else
for var in sequence:
    statement(var)
else:
    print("No items left.")

#%% for short
print(sequence)
output = [var == "B" for var in sequence]
print(output)

#%% while
i = 0
while i < 13:
    i += 1   
    statement("Tick: " + str(i))