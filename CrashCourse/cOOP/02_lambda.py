#%% displayHelper
from CrashCourse.displayhelper import *

#%% Lambda
myLambda = lambda arg: arg * 2

describe(myLambda)
print(myLambda(5))

#%% Example filter
new_list_filter = list(filter(lambda x: (x%2 == 0) , sequence))
print(new_list_filter)


#%% Example map
new_list_map = list(map(lambda x: x * 2 , sequence))
print(new_list_map)

#%%
