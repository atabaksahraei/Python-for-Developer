# python modules: https://docs.python.org/3/py-modindex.html
import sys
print(sys.version)


# import -> wird einmal vom Kernel ausgeführt; Funktionen sind verfügbar

##### import modules
# import hallo
# hallo.welt()
# hallo.mars()

##### import methods from modules
#from hallo import * !!!Nicht Empfehlenswert!!!
from hallo import welt, mars
welt()
mars()

# import matplotlib.pyplot
# matplotlib.pyplot.plot([1,2,3], [5,4,5])
# matplotlib.pyplot.show()

# from matplotlib import pyplot
# pyplot.plot([1,2,3], [5,4,5])
# pyplot.show()

import matplotlib.pyplot as plt # üblich...
plt.plot([1,2,3], [5,4,5])
# plt.show()

# from hallom import some_file as fl
# fl.f()


# from hallom import *
# some_file.f()

# import hallom
# hallom.some_file.f()


import hallom.some_file as myfile
myfile.f()