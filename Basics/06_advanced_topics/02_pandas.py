# import csv
# with open ("./names.csv", "r") as file:
#     fileReader = csv.reader(file, delimiter = ',')
#     for line in fileReader:
#         print (line)

import pandas as pd 
import numpy as np
df = pd.read_csv("./names.csv", sep=",", encoding="utf8", names=["Id", "Name", "Year", "Gender", "State", "Count"], skiprows=1,
dtype={"Id":np.int32, "Name":str, "Year":np.int32, "Gender":str, "State":str, "Count":np.int32})

print(df.head())

counter = 0
for id, row in df.iterrows():
    print (str(row.Id)+": " + str(type(row.Id)))
    print (row.Name+": " + str(type(row.Name)))
    print (str(row.Year)+": " + str(type(row.Year)))
    print (row.Gender+": " + str(type(row.Gender)))
    print (row.State+": " + str(type(row.State)))
    print (str(row.Count)+": " + str(type(row.Count)))
    counter += 1
    if counter > 3: break