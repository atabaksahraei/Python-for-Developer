#%% Operator overloading
class SdxArray():
    def __init__(self, list):
        self.__list = list

    def __mul__(self, num_2):
        return SdxArray([num * num_2 for num in self.__list])

    def __str__(self):
        return self.__list.__str__()

    def __getitem__(self, index):
        return self.__list[index] * -1

    def __repr__(self):
        return "SDX-AG:---->" + self.__str__()


array = SdxArray([1, 2, 3, 4, 5]) * 3
print(array)
print(array[0])

#%% Special Methods
# |    Operator | Expression                   | Internally                 |
# |------------:|------------------------------|----------------------------|
# | [index]     |   __getitem__(self, index)   |  Index operator            |
# | in          |   __contains__(self, value)  | Check membership           |
# | len         | __len__(self)                |  The number of elements    |
# | str         | __str__(self)                |  The string representation |

#%% Operator
# |            Operator | Expression | Internally          |
# |--------------------:|------------|---------------------|
# | Addition            | p1 + p2    | p1.__add__(p2)      |
# | Subtraction         | p1 - p2    | p1.__sub__(p2)      |
# | Multiplication      | p1 * p2    | p1.__mul__(p2)      |
# | Power               | p1 ** p2   | p1.__pow__(p2)      |
# | Division            | p1 / p2    | p1.__truediv__(p2)  |
# | Floor Division      | p1 // p2   | p1.__floordiv__(p2) |
# | Remainder (modulo)  | p1 % p2    | p1.__mod__(p2)      |
# | Bitwise Left Shift  | p1 << p2   | p1.__lshift__(p2)   |
# | Bitwise Right Shift | p1 >> p2   | p1.__rshift__(p2)   |
# | Bitwise AND         | p1 & p2    | p1.__and__(p2)      |
# | Bitwise OR          | p1 | p2    | p1.__or__(p2)       |
# | Bitwise XOR         | p1 ^ p2    | p1.__xor__(p2)      |
# | Bitwise NOT         | ~p1        | p1.__invert__()     |

#%% Comparison Operators
# |                 Operator | Expression | Internally        |
# |-------------------------:|------------|-------------------|
# | Less than                | p1 < p2    | p1.__lt__(p2)     |
# | Less than or equal to    | p1 <= p2   | p1.__le__(p2)     |
# | Equal to                 | p1 == p2   | p1.__eq__(p2)     |
# | Not equal to             | p1 != p2   | p1.__ne__(p2)     |
# | Greater than             | p1 > p2    | p1.__gt__(p2)     |
# | Greater than or equal to | p1 >= p2   | p1.__ge__(p2)     |
# | Remainder (modulo)       | p1 % p2    | p1.__mod__(p2)    |
# | Bitwise Left Shift       | p1 << p2   | p1.__lshift__(p2) |
# | Bitwise Right Shift      | p1 >> p2   | p1.__rshift__(p2) |
# | Bitwise AND              | p1 & p2    | p1.__and__(p2)    |
# | Bitwise OR               | p1 | p2    | p1.__or__(p2)     |
# | Bitwise XOR              | p1 ^ p2    | p1.__xor__(p2)    |
# | Bitwise NOT              | ~p1        | p1.__invert__()   |