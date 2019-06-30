#%%Tuple
#Tuple immutable (readonly)
t = ("Hans", 22, "IT")
print(t)
print(t[0])
name, age, subject = t
print (name)
print (age)
print (subject)

#%% Tuple unpacking
students = [
    ("Hans", 22, "IT"),
    ("Peter", 18, "Arts")
]

for student in students:
    name, age, subject = student
    print(name)

for name, age, subject in students:
    print (name)
