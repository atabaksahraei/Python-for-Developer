numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "noise ~}9?"]
print(numbers[-1]) # -> backwards

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