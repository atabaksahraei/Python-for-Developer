#%% displayHelper
from CrashCourse.displayhelper import *

#%% 
import matplotlib.pyplot as plt

def read():
    with open("./names.csv") as file:
        for line in file:
            yield line.strip().split(",")


def preview():
    counter = 0
    for row in read():
        counter += 1
        print(row)

        if counter >= 4:
            break


preview()

xs = []
ys = []

counter = 0
for row in read():
    counter += 1
    if counter == 1: continue
        
    xs.append(row[2])
    ys.append(row[5])

    if counter >= 1000: break

print(xs, ys)
plt.plot(xs, ys)
plt.show()
