# Python samples

## Blocks

In python blocks do not define scopes, however Functions, Objects, Modules do.

## Conditional statements

Python does not have switch/case, instead use elif statement.

## Loops I

Two loops; for & while.

## Class introspection

These functions work by using Class introspection:

- type()
- id()
- isinstance()

## Conditional Operators

1. **Comparison Operators**

    operator | py | desc
    ------- | ------- | -------
    == | a == b | Equal
    != | a != b | NotEqual
    < | a < b | Less than
    > | a > b | Greater than
    <= | a <= b | Less than or equal
    >= | a >= b | Greater than or equal

2. **Logical Operators**

    operator | py | desc
    ------- | ------- | -------
    and | x and y | True if both x and y
    or | x or y | True if x or y
    not | not x | Invert state

3. **Identity Operator**

    py | desc
    ------- | -------
    x is y | True if the same object
    x is not y | True if not the same object

4. **Membership Operators**

    py | desc
    ------- | -------
    x in y | True if x member of collection y
    x not in y | True if x not member of collection y

## Arithmetic Operators

desc | operator
------- | -------
Addition | +
Subtraction | -
Multiplication | *
Division | /
Integer Division | //
Remainder(modulo) | %
Exponent | **
Unary negative | -
Unary positive | +

```python
    # Unary operators
    z = -1
    z = +z
    print(z) # output: -1
```

## Bitwise Operators

desc | operator
------- | -------
And | &
Or | |
Xor | ^
Shift left | <<
Shift right | >>

## Loops II

You can use else in while, or for loop!

```python
    while pw != secret:
        if pw == '123': break
        pw = input('Enter secret word:')
    else: # in case while breaks, else won't run
        print('>Secret key is correct.')


    animals = ('bear', 'bunny', 'dog', 'cat')
    for pet in animals:
        print(pet)
    else:
        print('>Items finished.')
```

## Functions

### Arguments

To use argument lists, use *. For keyword arguments (a.k.a dictionary), use **

```python
    ## Argument list
    def func(*args):
        if len(args):
            for arg in args:
                print(arg)

    args = ('one', 'two', 'three')
    func(*args)

    # Keyword arguments or dictionary arguments
    def kitten(**kwargs):
        if len(kwargs):
            for k in kwargs:
                print(f'Kitten {k} says {kwargs[k]}')

    x = dict(Buffy='meow', Zilla='grr', Angel='rawr')
    kitten(**x)
```

### Generators

range() is an example of generators, it is useful for creating a series of values. It uses *yield* return.

```python
    def inclusive_range(*args):
        ...
        i = start
        while i <= stop:
            yield i
            i += step
```

### Decorators

```python
    def f1(f):
        def f2():
            print('before function call')
            f()
            print('after function call')
        return f2

    @f1
    def f3():
        print('this is f3')

    f3()
```
