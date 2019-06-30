#%% displayHelper
from CrashCourse.displayhelper import *

#%% Class
from datetime import date

class Person:
    
    # static attribute
    global_id = 0

    def __init__(self, name, birthday): # constructor
    
        # instance attribute
        self.__id = Person.global_id        # private
        self._birthday = birthday           # protected
        self.name = name                    # public
        self.age = date.today().year - birthday.year

        # static attribute
        Person.global_id += 1

    # instance method
    def Hi(self):
        print("{}:Hi :)".format(self.__id))

    def __format__(self, format):
        if format == "D":
            return "{}:{} is {} years old.".format(self.__id, self.name, self.age)
        elif format == None:    
            return "{} is {} years old.".format(self.name, self.age)

        return "{}:{} ({}).".format(self.__id, self.name, format)

    def __str__(self):
        return self.__format__("__str__")
            
    def __repr__(self):
        return self.__format__("__repr__")

    def __len__(self):
        return 1234

        
        

person = Person("Atabak", date(1990, 9, 19))

#%% Encapsulation
person.Hi()

#%% __format__
print("User: {:D}".format(person))
print("User: {}".format(person))

#%% __str__
print(str(person))
print(person)

#%% __repr__
person # type in console

#%% __len__
print(len(person))

#%% Deleting Attributes
del person.name
print(person)