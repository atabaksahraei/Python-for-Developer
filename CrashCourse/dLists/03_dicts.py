#%% displayHelper
%cd ".."
from displayhelper import *

#%% dicts
d = { "Berlin":123, "Helsinki":456, "Muenchen": 890 }
print (d)
print(d["Berlin"])
print(d.get("Berlin"))
print(d.get("NOPE"))

d["Friedberg"] = 100
print (d)

# multidimension
students  ={
    "IT": ["Hans", "Peter"],
    "BWL": ["Sven", "Svenja"]
}
describe(students)
describe(students["IT"])

#%% dict -> del entry
del d["Berlin"]
print(d)

#%% dict in objects
class Me:
    pass
me = Me()
describe(me.__dict__)
me.nAme = "myName"
me.Name = "myName"
describe(me.__dict__)
del me.nAme
describe(me.__dict__)

wait = ""
#%% dict if
if "Friedberg" in d: print("Friedberg matched")
if "Berlin" in d: print("Berlin matched")

#%% dict tupple
d = { "Berlin":123, "Helsinki":456, "Muenchen": 890 }

for key in d:
    print(key)

print (d.items())

for key, value in d.items():
    print (key + ": " + str(value))


