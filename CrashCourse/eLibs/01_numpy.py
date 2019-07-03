#%% why numpy
array = []
for i in range(0, 10):
    array.append(i**2)

array = [i**2 for i in range(0, 10)]

#%% array
import numpy as np # np->convention

np_zero = np.zeros(4)
np_array = np.array([0, 1, 2, 3, 10])
np_arange = np.arange(10) ** 2 #-> operator overloading

#%% math lib
min = np_array.min()
max = np_array.max()
mean = np_array.mean()
std = np_array.std()


#%% Filter
a = np.array([1, 2, 3, 4])
b = np.array([True, False, False, True])
a[b]

a[a % 2==0]

# Multidimension
#%% Reshape []->[][]
a = np.arange(8)
tuple = (4, 2)
reshape = a.reshape(tuple)
print(reshape)
print(reshape[0])
print(a.reshape((-1, 2)))

#%% Reshape-> [][]->[]
b = np.array([[1, 2, 3], [4, 5, 6]])
b.reshape(-1)

#%% Reshape describe
print(b.shape)
print(a.shape)
