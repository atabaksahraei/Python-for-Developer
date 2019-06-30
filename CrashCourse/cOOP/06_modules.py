
# python modules
# https://docs.python.org/3/py-modindex.html
import sys
print(sys.version)

## import 
# -> wird einmal vom Kernel ausgeführt; Funktionen sind verfügbar

# import modules
import hello
hello.welt()
hello.mars()

# import methods
from hello import welt, mars
welt()
mars()

# hellom
from hellom import some_file as fl
fl.f()


from hellom import * # !!!Nicht Empfehlenswert!!!
some_file.f()

import hellom
hellom.some_file.f()


import hellom.some_file as myfile
myfile.f()
