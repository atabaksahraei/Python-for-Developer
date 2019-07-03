#%% inheritance
from datetime import date
from dateutil.parser import parse as date_parser

class Person:
    global_id = 0

    def __private(self):
        print("private")

    def _protected(self):
        print("protected")

    def __init__(self, name, birthday):
        self.__id = Person.global_id
        self._birthday = date_parser(birthday)
        self.name = name
        self.age = date.today().year - self._birthday.year
        Person.global_id += 1


class Student(Person):
    def __init__(self, name, birthday, term):
        super().__init__(name, birthday)
        self.__term = term
        # self.__private()
        self._protected()

    def increase_term(self):
        self.__term += 1

class Worker(Person):
    def __init__(self, name, birthday, taxId , company):
        super().__init__(name, birthday)
        self.taxId = taxId
        self.company = company
        self.hours = 0

    def work(self):
        self.hours +=1

person = Person("Atabak", "1990-9-19")
student = Student("Atabak", "1990-9-19", 5)
worker = Worker("Atabak", "1990-9-19", 5987654, "SDX-AG")

student._protected()
student.increase_term()
# student.__private()

#%% multiple inheritance
# https://www.python-course.eu/python3_multiple_inheritance.php

#%% Method Resolution Order :´(
class WorkingStudent(Student, Worker):
    def __init__(self, name, birthday, term, taxId, company):
        super().__init__(name, birthday, term)
        self.taxId = taxId
        self.company = company
        self.hours = 0

print(WorkingStudent.mro())
working_student = WorkingStudent("Atabak", "1990-9-19", 5, 987654, "SDX-AG")


#%% datacamp: TextDescriber
# https://www.datacamp.com/community/tutorials/super-multiple-inheritance-diamond-problem
class Tokenizer:
    """Tokenize text"""
    def __init__(self, text):
        print('Start Tokenizer.__init__()')
        self.tokens = text.split()
        print('End Tokenizer.__init__()')


class WordCounter(Tokenizer):
    """Count words in text"""
    def __init__(self, text):
        print('Start WordCounter.__init__()')
        super().__init__(text)
        self.word_count = len(self.tokens)
        print('End WordCounter.__init__()')


class Vocabulary(Tokenizer):
    """Find unique words in text"""
    def __init__(self, text):
        print('Start init Vocabulary.__init__()')
        super().__init__(text)
        self.vocab = set(self.tokens)
        print('End init Vocabulary.__init__()')


class TextDescriber(WordCounter, Vocabulary):
    """Describe text with multiple metrics"""
    def __init__(self, text):
        print('Start init TextDescriber.__init__()')
        super().__init__(text)
        print('End init TextDescriber.__init__()')

print(TextDescriber.mro())
td = TextDescriber('row row row your boat')
print('--------')
print(td.tokens)
print(td.vocab)
print(td.word_count)

#%%
