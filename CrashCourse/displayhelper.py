def describe(myVar):
    print(myVar, "is of type", type(myVar))

def display_ref(ref):
    print("The ref is: " + str(id(ref)))

def display_ev(desc, term):
    print(desc + ": " + str(term))


condition = True
def statement(stuff="DEFAULT"):
    print(stuff)

sequence = [1, 2, 3, 4]