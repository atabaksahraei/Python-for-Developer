numbers = ["one", "two", "three", "four", "ABC", "DEF"]
print(numbers[-1]) # ->von hinten

#list slicing
print(numbers[2:4]) 
print(numbers[1:-1]) 
print(numbers[0:-1]) #0 kann weggelassen werden
print(numbers[:-1])
print(numbers[1:])

print("Hallo Welt"[:5])
print("Hallo Welt"[-4:])
print("Hallo Welt"[:])

# [:] -> slice
# [wo möchte ich anfange: wo möchte ich aufhören]

#list comprehensions
xs = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ys = [x*x for x in xs]
# ys = []
# for x in xs:
#     ys.append(x*x)

print(xs)
print(ys)

counts = [len(n) for n in numbers]
print (counts)

xs = [x/10 for x in range(0, 100)]
print(xs)


#dicts
d = { "Berlin":123, "Helsinki":456, "Muenchen": 890 }
print (d)
print(d["Berlin"])
print(d.get("Berlin"))
print(d.get("NOPE"))

d["Friedberg"] = 100
print (d)

del d["Berlin"]
print(d)

if "Friedberg" in d: print("Friedberg matched")
if "Berlin" in d: print("Berlin matched")



#Tuple immutable (readonly)
t = ("Hans", 22, "IT")
print(t)
print(t[0])
name, age, subject = t
print (name)
print (age)
print (subject)

students = [
    ("Hans", 22, "IT"),
    ("Peter", 18, "Arts")
]

# for student in students:
#     name, age, subject = student
#     print(name)
for name, age, subject in students:
    print (name)


# dict tupple
d = { "Berlin":123, "Helsinki":456, "Muenchen": 890 }

for key in d:
    print(key)

print (d.items())
for key, value in d.items():
    print (key + ": " + str(value))

# multidimension
list = [
    ["Berlin", "Muenchen", "Koeln"],
    ["Budapest", "CDE", "EFG"]
]

print(list[0][1])

students  ={
    "IT": ["Hans", "Peter"],
    "BWL": ["Sven", "Svenja"]
}
print(students["IT"])