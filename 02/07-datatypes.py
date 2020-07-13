from decimal import *

# python uses dynamic typing a.k.a duck typing.
# Type of the value is determined by the value itself


def stringSamples():
    # multiline string
    multiLine = ''' 
    seven 
    '''

    # formating a string
    formated = 'seven {} {}'.format(8, 9)
    # swap positions
    formated2 = 'seven {1} {0}'.format(8, 9)

    # add spaces after or before
    formated3 = 'seven {:<9} {:>9}'.format(8, 9)

    # add zeros after or before a string
    formated4 = 'seven {:<09} {:>09}'.format(8, 1234)

    # using f string
    a = 1
    formatted5 = f'seven {a:<09}'

    print(formated4)

    x = 'seven'.upper()

    print(f"x is {x}")
    print(type(x))


def numberSamples():
    # the result will be float by default
    x = 7 / 3

    # if you want an int result use this
    y = 7 // 3
    print(y)
    print(type(y))

    # dealing with monetary values
    a = Decimal('.10')
    b = Decimal('.30')
    r = a + a + a - b
    print(r)
    print(type(r))


def boolSamples():
    # 0, "", None are evaluated as False
    # 1, "x", are evaluated as True
    x = None
    print(x)
    print(type(x))

    if x:
        print(True)
    else:
        print(False)


def sequenceTypeSamples():
    # Lists (mutable)
    x = [1, 2, 3, 4, 5]
    x[2] = 42
    for i in x:
        print(f'i is {i}')

    # Tuples (immutable)
    y = (1, 2, 3, 4, 5)
    for i in y:
        print(f'i is {i}')

    # Range is a continues sequence (immutable), starts from 0 to n-1
    r = range(5)
    # OR you can change the starting point, start from 2 to 4
    r2 = range(2, 5)
    # OR you can change the step. e.g 2 7 12 17 ... 47
    r3 = range(2, 50, 5)
    # you can make range mutable by using list
    r4 = list(range(5))
    r4[2] = 42
    for i in r4:
        print(f'i is {i}')

    # Dictionary {key: value}, (mutable)
    d = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
    d['three'] = 42
    for k, v in d.items():
        print(f'k:{k}, v:{v}')


def typeAndId():
    x = (1, 'two', 3.0, [4, 'four'], 5)
    y = (1, 'two', 3.0, [4, 'four'], 5)

    # class introspection
    ## type represents object's types
    print(type(x))
    print(type(y))

    ## id represents unique identification of objects
    # id(x) and id(y) are different.
    print(id(x))
    print(id(y))
    # but id(x[0]) and id(y[0]) are same ! python doesn't create a new object when it's already made
    print(id(x[0]))
    print(id(y[0]))

    ## to check if one object is the same instance of other object
    if x[0] is y[0]:
        print('yep')
    else:
        print('nope')

    ## to check if type of an object is specific type
    if isinstance(x, tuple):
        print('tuple')
    elif isinstance(x, list):
        print('list')
    else:
        print('nope')


typeAndId()
