#%% inheritance
from datetime import date
from dateutil.parser import parse as date_parser

class Person:
    global_id = 0

    def __private(self):
        print("private")

    def _protected(self):
        print("protected")

    def __init__(self, name, birthday): # constructor
        self.__id = Person.global_id
        self._birthday = date_parser(birthday)
        self.name = name
        self.age = date.today().year - self._birthday.year
        Person.global_id += 1


class Student(Person):
    def __init__(self, name, birthday, term):
        super().__init__(name, birthday)
        self.__term = term
        #self.__private()
        self._protected()

    def increase_term(self):
        self.__term += 1

class Worker(Person):
    def __init__(self, name, birthday, company):
        super().__init__(name, birthday)
        self.company = company


student = Student("Atabak", "1990-9-19", 5)
worker = Worker("Atabak", "1990-9-19", "SDX-AG")

student._protected()
student.increase_term()
#student.__private()

#%% multiple inheritance