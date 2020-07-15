# string is immutable
s1 = 'hello'
s2 = s1.upper()
print(f'{id(s1)}, {id(s2)}')

# string concatenation 1
print(s1 + ' ' + s2)
# string concatenation 2
s3 = 'first' ' second'
print(s3)

print('hello'.upper())
print('HELLO'.lower())

print('Hello'.swapcase())

# forces lower cases to unicode characters as well
print('Hello'.casefold())

# capitalize the first word e.g. Hello world
print('hello world'.capitalize())
# capitalize the first char of each word e.g. Hello World
print('hello world'.title())

print("""
    hello 
    {}
""".format(42 * 7))


class RevString(str):
    def __str__(self):
        return self[::-1]


s = RevString('Hello')
print(s)
