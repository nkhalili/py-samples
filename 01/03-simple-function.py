# define a basic function
def func1():
    print("I am a function")


# direct invocation, execute the content of a function
func1()
# called inside the print function, because there is no return value it prints None
print(func1())
# printing the function definition itself and not the content (functions are objects)
print(func1)
