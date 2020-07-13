# Argument list
def func(*args):
    if len(args):
        for arg in args:
            print(arg)


func(1, 2, 3)

# if you want to send tuple or list as arguments use asterisk to send them individually
# args = [1, 2, 3, 4]
args = ('one', 'two', 'three')
func(*args)

# Keyword arguments (this is dictionary)


def kitten(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print(f'Kitten {k} says {kwargs[k]}')


x = dict(Buffy='meow', Zilla='grr', Angel='rawr')
kitten(**x)

# Generators


def inclusive_rang(*args):
    length = len(args)
    start = 0
    step = 1

    if length < 1:
        raise TypeError(f'Expected parameters are less than 1. got {length}')
    elif length == 1:
        stop = args[0]
    elif length == 2:
        (start, stop) = args
    elif length == 3:
        (start, stop, step) = args
    else:
        raise TypeError(f'Expected three parameters but got {length}')

    i = start
    while i <= stop:
        yield i
        i += step


for i in inclusive_rang(5):
    print(i, end=' ')


# Decorator
def f1(f):
    def f2():
        print('before function call')
        f()
        print('after function call')
    return f2

# Sends f3 as a parameter into f1
@f1
def f3():
    print('this is f3')

f3()
