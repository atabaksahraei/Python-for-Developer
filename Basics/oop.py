# convention
# private -> __varName, __methodName
# private -> __
# protected -> _

class Student():
    global_id = 1
    def __init__ (self, firstname, lastname):
        self.firstname = firstname 
        self.lastname = lastname 
        self.__term = 1
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

    def __str__(self):
        return str(self._id) + ": "+self.get_name()

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return self.__term

class WorkingStudent(Student):
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