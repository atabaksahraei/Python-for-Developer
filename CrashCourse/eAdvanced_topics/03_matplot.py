#%% displayHelper
from CrashCourse.displayhelper import *

#%% Backend
# %matplotlib notebook
# %matplotlib inline
# external window
# %matplotlib tk
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [5, 4, 4.5])
plt.show()

#%% style
# https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot
plt.plot([1, 2, 3], [5, 4, 4.5], color="#ff9900", marker="o", linestyle="dashed", label="SomeNumbers")
plt.legend()
plt.show()

#%% Pie
plt.pie([1, 2, 3])
plt.show()

#%% Bar
plt.bar([1,2,3],[5,6,5])
plt.show()

#%%Scatter
plt.scatter([1,2,3],[5,6,5])
plt.show()

#%% violinplot
plt.violinplot([1.2,2.1,3.87])
plt.show()

#%%
