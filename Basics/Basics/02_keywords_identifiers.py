#%% Keywords
import keyword
print(keyword.kwlist)

#%% Keywords-Example
print("1 == 1" + ": " + str(1 == 1))
print("5 > 3" + ": " + str(5 > 3))
print("True or False" + ": " + str(True or False))
print("10 <= 1" + ": " + str(10 <= 1))
print("3 > 7" + ": " + str(3 > 7))

#%% Keywords-Example-TrueFalse
print("True and False" + ": " + str(True and False))
print("True == 1" + ": " + str(True == 1))
print("False == 0" + ": " + str(False == 0))
print("True + True" + ": " + str(True + True))

#%% Keywords-Example-None
# is null in c#
print(" None == 0" + ": " + str( None == 0))
print("None == []" + ": " + str(None == []))
print("None == False" + ": " + str(None == False))
print("None == None" + ": " + str(None == None))


#%% Identifier
# PascalCase: IchBesteheAusMehrerenWoertern
# camelCase: ichBesteheAusMehrerenWoertern
# snake_case: ich_bestehe_aus_mehreren_woertern
class PascalCase():
    my_static_snake_case = 56

    def __init__(self, my_var=2.478):
        self.__my_private_var = my_var
        self._my_protected_var = self.__my_private_var * PascalCase.my_static_snake_case
        self.my_public_var = self._my_protected_var % 2

    def snake_case(self):
        print("ich_bestehe_aus_mehreren_woertern")
        # camelCase -> Wird in Python nicht benutzt

PascalCase.my_static_snake_case
pascal_case = PascalCase()
#print(pascal_case.__my_private_var)
print(pascal_case._my_protected_var)
print(pascal_case.my_public_var)
