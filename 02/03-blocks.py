x = 42
y = 73

# Blocks define by indentation e.g. 4 spaces

if x < y:
    z = 100
    print("x < y: x is {}, y is {}".format(x, y))

## in python blocks do not define scope, Functions, objects, module DO.
# z has the same scope as x and y even though its block is different!
print("z is: ", z)
