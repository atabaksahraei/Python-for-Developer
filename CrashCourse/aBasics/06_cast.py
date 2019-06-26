#%% Cast -> int()
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
print(type(x))
print(type(y))
print(type(z))
if(type(x) == int): print("it is a int")
if(type(x) == str): print("it is a string")
if(type(x) == float): print("it is a float")

#%% Cast -> float()
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
print(type(x))
print(type(y))
print(type(z))
if(type(x) == int): print("it is a int")
if(type(x) == str): print("it is a string")
if(type(x) == float): print("it is a float")

#%% Cast -> str()
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
print(type(x))
print(type(y))
print(type(z))
if(type(x) == int): print("it is a int")
if(type(x) == str): print("it is a string")
if(type(x) == float): print("it is a float")


#%% round()
print(round(10))
print(round(10.7))
print(round(5.5))
print(round(2.665, 2))
print(round(2.675, 2))