
#%% python modules
# https://docs.python.org/3/py-modindex.html
import sys
print(sys.version)


#%% import 
# -> wird einmal vom Kernel ausgeführt; Funktionen sind verfügbar

#%% import modules
# import hello as hello
import CrashCourse.cOOP.hello as hello
hello.welt()
hello.mars()

#%% import methods
#from hello import * !!!Nicht Empfehlenswert!!!
from hello import welt, mars
from hello import welt, mars
welt()
mars()

#%% matplotlib.pyplot
# matplotlib.pyplot.plot([1,2,3], [5,4,5])
# matplotlib.pyplot.show()

# from matplotlib import pyplot
# pyplot.plot([1,2,3], [5,4,5])
# pyplot.show()

import matplotlib.pyplot as plt # üblich...
plt.plot([1,2,3], [5,4,5])
# plt.show()

#%% hellom
# from hellom import some_file as fl
# fl.f()


# from hellom import *
# some_file.f()

# import hellom
# hellom.some_file.f()


import hellom.some_file as myfile
myfile.f()

#%%
