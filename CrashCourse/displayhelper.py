def describe(myVar):
    print(myVar, "is of type", type(myVar))

def display_ref(myVar):
    print(myVar, "ref is: " + str(id(myVar)))

def display_ev(desc, term):
    print(desc + ": " + str(term))


condition = True
def statement(stuff="DEFAULT"):
    print(stuff)

sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]