# function that takes arguments
def func2(arg1, arg2):
    print(arg1, "", arg2)

# function that returns a value


def cube(x):
    return x*x*x


func2(10, 20)
print(func2(10, 20))
print(cube(3))

# function with default parameter value


def power(num, x=1):
    result = 1
    for i in range(x):
        result *= num
    return result


print(power(2))
print(power(2, 3))
# parameters are interchangeable
print(power(x=3, num=2))


# function with variable parameter
def multi_add(*args):
    result = 0
    for x in args:
        result += x
    return result


print(multi_add(2, 3, 4, 5, 6))
