# https://www.programiz.com/python-programming/object-oriented-programming
class Student(): #-> PascalCase
    global_id = 1 #-> sneak_case
    def __init__ (self, firstname, lastname):
        self.firstname = firstname 
        self.lastname = lastname 
        # private -> __varName, __methodName
        self.__term = 1 

        # protected -> _
        self._id = Student.global_id

        Student.global_id += 1

    def get_term(self):
        return self.__term

    def increase_term(self):
        self.__term +=1

    def get_name(self):
        return self.firstname +" | "+ self.lastname

    def print_info(self):
        print(self.get_name() + "(Term: "+ str(self.__term) + ")")

    # >>> print(l)  # calls __str__
    def __str__(self):
        return str(self._id) + ": "+self.get_name()

    # >>> l  # calls __repr__
    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return self.__term


#%% Inheritance
class Worker():
    isWorker = true
    pass

class WorkingStudent(Student, Worker): # Multiple Inheritance
    def __init__(self, firstname, lastname, company):
        super().__init__(firstname, lastname)
        self.company = company

    def __str__(self):
        return super().__str__() + " (Working in " + self.company + ")"


jens = WorkingStudent("jens", "Mueller", "ABC AG")
monika = Student("monika", "Musterfrau")

jens.increase_term()
jens.increase_term()
jens.increase_term()
print (jens.get_term())

print(jens)
print(monika)
print(len(jens))