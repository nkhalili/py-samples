import sys


def main():
    try:
        x = int('foo')
        y = 5 / 2
        raise TypeError('This is a sample throw error')
    except ValueError as e:
        # output: a value error: invalid literal for int() with base 10: 'foo'
        print(f'a value error: {e}')
    except ZeroDivisionError:
        print('don\'t divide by zero')
    except:
        # to get some info about error
        print(f'something goes wrong {sys.exc_info()}')
        # to show exactly what's the problem
        print(f'something goes wrong {sys.exc_info()[1]}')
    else:
        print('no errors')


if __name__ == "__main__":
    main()
