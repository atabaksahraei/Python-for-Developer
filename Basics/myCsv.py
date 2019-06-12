# python modules: https://docs.python.org/3/py-modindex.html
import sys
print(sys.version)

# import csv
# with open ("./Kursmaterialien/data/names.csv", "r") as file:
#     fileReader = csv.reader(file, delimiter = ',')
#     for line in fileReader:
#         print (line)

import pandas as pd 
import numpy as np
df = pd.read_csv("./Kursmaterialien/data/names.csv", sep=",", encoding="utf8", names=["Id", "Name", "Year", "Gender", "State", "Count"], skiprows=1,
dtype={"Id":np.int32, "Name":str, "Year":np.int32, "Gender":str, "State":str, "Count":np.int32})

print(df.head())

for  id, row in df.iterrows():
    print (str(row.Id)+": " + str(type(row.Id)))
    print (str(row.Name)+": " + str(type(row.Name)))
    print (str(row.Year)+": " + str(type(row.Year)))
    print (str(row.Gender)+": " + str(type(row.Gender)))
    print (str(row.State)+": " + str(type(row.State)))
    print (str(row.Count)+": " + str(type(row.Count)))