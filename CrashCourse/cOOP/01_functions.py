#%% displayHelper
%cd ".."
from displayhelper import *

#%% func
def funcname(parameter, default_param=10, default_2_param=None):
    """This func execute a statement."""
    statement(parameter)

    if default_2_param is not None:
        statement(default_param)

funcname(True)
funcname(True, 30, "ABC")


#%% return
def absolute_value(num):
    """This function returns the absolute
    value of the number"""
    if num >= 0:
        return num
    else:
        return -num

abs = absolute_value(-4)
print(abs)

#%% Scope and Lifetime
def my_func():
	x = 10
	print("Value inside my_func:", x)

def my_func_2():
	print("Value inside my_func_2:", x)

x = 20
my_func()
my_func_2()
print("Value outside function:", x)
