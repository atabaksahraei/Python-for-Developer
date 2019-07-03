#%% displayHelper
from CrashCourse.displayhelper import *

#%% decorator pattern
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("I am ordinary")

ord = ordinary
describe(ord)

inner = make_pretty(ord)
describe(inner)

inner()

#%% decorator in python
# args:
#        is a tuple of positional arguments,
#        because the parameter name has * prepended.

# kwargs:
#        is a dictionary of keyword arguments,
#        because the parameter name has ** prepended.

def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner

@star
@percent
def printer(msg):
    print(msg)

printer("Hello")