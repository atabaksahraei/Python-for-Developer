def describe(myVar):
    print(myVar, "is of type", type(myVar))

def display_ref(myVar):
    print(myVar, "ref is: " + str(id(myVar)))

def display_ev(desc, term):
    print(desc + ": " + str(term))

import inspect
def nameof(var):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return [var_name for var_name, var_val in callers_local_vars if var_val is var]

condition = True

def statement(stuff="DEFAULT"):
    print(stuff)

sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]