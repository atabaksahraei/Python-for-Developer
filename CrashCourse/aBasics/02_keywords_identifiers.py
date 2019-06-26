#%% displayHelper
from CrashCourse.displayhelper import *

#%% Keywords
import keyword
print(keyword.kwlist)

#%% Keywords-Example
display_ev("1 == 1", 1 == 1)
display_ev("5 > 3", 5 > 3)
display_ev("True or False", True or False)
display_ev("10 <= 1", 10 <= 1)
display_ev("3 > 7", 3 > 7)

#%% Keywords-Example-TrueFalse
display_ev("True and False", True and False)
display_ev("True == 1", True == 1)
display_ev("False == 0", False == 0)
display_ev("True + True", True + True)

#%% Keywords-Example-None
# is null in c#
display_ev("None == 0" , None == 0)
display_ev("None == []" , None == [])
display_ev("None == False" , None == False)
display_ev("None == None" , None == None)


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
