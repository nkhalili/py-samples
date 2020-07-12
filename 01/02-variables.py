# variables
f = 0
print(f)

# re-declaring variables
f = "abc"
print(f)

# differnet variable types CANNOT be combined. No implicit conversion
## print("this is a string " + 123)
print("this is a string " + str(123))

# global vs. local variables in functions


def someFunction():
    # to use your flobal variable
    global f
    f = "def"
    print(f)


someFunction()
print(f)

# to undefine/remove a variable 
# del f
print(f)
