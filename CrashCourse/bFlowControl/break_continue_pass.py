#%% displayHelper
from CrashCourse.displayhelper import *

#%% break
i = 0
while True:
    i += 1
    statement("Tick: " + str(i))
    if i > 3: break

#%% continue
i = 0
while i < 13:
    i += 1   
    if (i % 2) == 0: continue
    statement("Tick: " + str(i))

#%% pass
# pass is a null statement
def funcname(parameter_list):
    pass