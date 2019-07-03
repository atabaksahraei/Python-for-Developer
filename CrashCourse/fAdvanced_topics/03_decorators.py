#%% displayHelper
from CrashCourse.displayhelper import *

#%% decorator pattern
def make_pretty(func, msg):
    message = msg
    def inner(): # closures: inner func which has access to local scope
        print("I got decorated: {}".format(msg))
        func()
    return inner

def ordinary():
    print("I am ordinary")

describe(ordinary)

inner = make_pretty(ordinary, "Hi :)")
describe(inner)

inner()
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