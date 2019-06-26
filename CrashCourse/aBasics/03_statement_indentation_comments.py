#%% Statement
a = 1; b = 2; c = 3

#%% Multi-line statement
a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9

a = (1 + 2 + 3 +
    4 + 5 + 6 +
    7 + 8 + 9)

colors = ['red',
      'blue',
      'green']

#%% Indentation
# Most of the programming languages like C, C++, Java
# use braces { } to define a block of code.
# Python uses indentation.
for i in range(1,11):
    print(i)
    if i == 5:
        break

#%% Comments
# this is a comment