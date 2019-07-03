#%% displayHelper
from CrashCourse.displayhelper import *

#%% why pandas
import csv
with open ("./data/tips.csv", "r") as file:
     fileReader = csv.reader(file, delimiter = ',')
     counter = 0
     for line in fileReader:
         print (line)
         counter += 1
         if counter > 5:
             break

#%% read csv
import pandas as pd

df = pd.read_csv("./data/tips.csv")
df.head()

#%% read excel
df = None
df = pd.read_excel("./data/tips.xlsx", sheet_name="billdata")
print(len(df))
df.head()

#%% access to dataframe
describe(df["tip"]) #column
describe(df.iloc[0]) #row
describe(df.iloc[0]["sex"]) #multidimension array
describe(df.iloc[:5]["sex"]) #list slicing

#%% as tupple
for pos, d in df.iterrows():
    print (pos)
    describe(d)
    total_bill, tip, sex, smoker, day, time, size = d
    print(total_bill)
    break

#%% Filter
male = df[df["sex"] == "Male"]
print(len(male))
male.head()

#%% Ordering
df_sorted = df.sort_values("tip", ascending=False)
df_sorted.head()

#%% Plot
import matplotlib.pyplot as plt
data = [(day, df[df["day"]==day]["tip"].sum()) for day in set(df["day"])] #filter
data = pd.DataFrame(data) # new df
data.rename(columns={0:"day", 1:"tip_sum"}, inplace=True) #inplace
print(data)
plt.plot(data["day"], data["tip_sum"])
plt.legend() # label
plt.show()

#%%
