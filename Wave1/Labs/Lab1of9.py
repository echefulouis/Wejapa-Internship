# Browse the complete list of string methods at:
# https://docs.python.org/3/library/stdtypes.html#string-methods 
# and try them out here. Endeavor to copy the link without the first # comment sign beginning it.

#Class Range
print (list(range(10)))

#.format
print("The sum of 1 + 2 is {0}".format(1+2))

#find function
print('py' in 'python')

#is identifier
from keyword import iskeyword
print('hello'.isidentifier(), iskeyword('hello'))
print('def'.isidentifier(), iskeyword('def'))

#is Lowwer
print('is'.islower())

#isStrip
print('   spacious   '.lstrip())

#upper()
print('Hello World'.upper())