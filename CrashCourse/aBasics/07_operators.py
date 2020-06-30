#%% displayHelper
%cd ".."
from displayhelper import *

#%% Arithmetic
# | Operator | Description     |
# |----------|-----------------|
# | +        | Add             |
# | -        | Subtract        |
# | *        | Multiply        |
# | /        | Divide          |
# | %        | Modulus         |
# | //       | Floor division  |
# | **       | Exponent        |

x = 14
y = 3

print('x + y =',x+y)
print('x - y =',x-y)
print('x * y =',x*y)
print('x / y =',x/y)
print('x // y =',x//y)
print('x ** y =',x**y)

#%% Comparison
# | Operator | Description      |
# |----------|------------------|
# | >        | Greater          |
# | <        | Less             |
# | ==       | Equal            |
# | !=       | Not equal        |
# | >=       | Greater or equal |
# | <=       | Less or equal    |

#%% Logical
# | Operator | Description           |
# |----------|-----------------------|
# | and      | True if both are true |
# | or       | True if one is true   |
# | not      | True if is false      |

#%% Assignment
# | Operator | Example | Equivatent to |
# |----------|---------|---------------|
# | =        | x = 5   | x = 5         |
# | +=       | x += 5  | x = x + 5     |
# | -=       | x -= 5  | x = x - 5     |
# | *=       | x *= 5  | x = x * 5     |
# | /=       | x /= 5  | x = x / 5     |
# | %=       | x %= 5  | x = x % 5     |
# | //=      | x //= 5 | x = x // 5    |
# | **=      | x **= 5 | x = x ** 5    |
# | &=       | x &= 5  | x = x & 5     |
# | |=       | x |= 5  | x = x | 5     |
# | ^=       | x ^= 5  | x = x ^ 5     |
# | >>=      | x >>= 5 | x = x >> 5    |
# | <<=      | x <<= 5 | x = x << 5    |

#%% Bitwise
# x = 10 (0000 1010)
# y =  4 (0000 0100)
# | Operator | Description         | Example                 |
# |----------|---------------------|-------------------------|
# | &        | Bitwise AND         | x& y  =   0 (0000 0000) |
# | |        | Bitwise OR          | x | y =  14 (0000 1110) |
# | ~        | Bitwise NOT         |    ~x = -11 (1111 0101) |
# | ^        | Bitwise XOR         | x ^ y =  14 (0000 1110) |
# | >>       | Bitwise right shift | x>> 2 =   2 (0000 0010) |
# | <<       | Bitwise left shift  | x<< 2 =  40 (0010 1000) |