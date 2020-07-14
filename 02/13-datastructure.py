from math import pi

# List
def listAndTupleSample():
    ### list (mutable)
    game = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

    # tuple (immutable) cannot use .append()
    # game = ('Rock', 'Paper', 'Scissors', 'Lizard', 'Spock')

    print(game[1])  # output: paper
    print(game[1:3])  # output: ['Paper', 'Scissors']
    print(game[1:5:2])  # like range() output: ['Paper', 'Lizard']

    # to get index of an item in the list
    i = game.index('Paper')
    print(game[i])

    # list is mutable
    game.append('Computer')  # adds to the end of the list
    game.insert(0, 'Computer')  # adds to the particular index

    # to remove item from the list
    game.remove('Paper')
    x = game.pop()  # remove the last item and return it (like STACK)
    print(x)
    game.pop(3)  # remove at particular index by using pop()
    del game[3]  # remove at particular index by using del statement
    del game[1:5:2]  # remove by slice

    # to join items in game separated by comma
    print(', '.join(game))

    # to get the length of list using len() function
    print(len(game))

    for i in game:
        print(i, end=' ', flush=True)


def dictSample():
    # The first way to create a dictionary
    animals = {'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr',
               'giraffe': 'I am a giraffe!', 'dragon': 'rawr'}

    # another way to define dictionary using dict constructor and keyword arguments
    animals2 = dict(kitten='meow', puppy='ruff!', lion='grrr',
                    giraffe='I am a giraffe!', drafon='rawr')

    # to loop through dict items, two ways
    # for x in animals:
    #     print(f'{x}: {animals[x]}')
    for k, v in animals.items():
        print(f'{k}: {v}')

    # to loop through just dict keys
    for k in animals.keys():
        print(k)
     # to loop through just values
    for v in animals.values():
        print(v)

    # to pick an item
    print(animals['lion'])

    # to change an item's value
    animals['lion'] = 'I am a lion!'

    # to add a new item
    animals['monkey'] = 'haha'

    # to search for a key
    print('lion' in animals)
    print('found!' if 'lion' in animals else 'nope!')

    # if an item does not exists this *will raise an exception*
    print(animals['godzilla'])

    # to see if an item exists, if not returns None *without exceptions*
    print(animals.get('godzilla'))


def setSample():
    a = set("set1")
    b = set("set2")

    # to sort a set, everytime that you run it it's same result
    print(sorted(a))

    # set differentiate, or, xor
    print_set(a - b)  # output: is {1}
    print_set(a | b)  # output: is {set12}
    print_set(a ^ b)  # output: is {12}
    print_set(a & b)  # output: is {tse}


def print_set(o):
    print('{', end='')
    for x in o:
        print(x, end='')
    print('}')


seq = range(11)

# create a new list with each element times two
seq2 = [i * 2 for i in seq]

# create a new list with a condition
seq3 = [i for i in seq if i % 3 != 0]

# create tuples instead of each item
seq4 = [(i, i**2) for i in seq]

# using a function
seq5 = [round(pi, i) for i in seq]

# create a dictionary
seq6 = {i: i**2 for i in seq}
seq7 = { x for x in 'superduper' if x not in 'pd'}

print(seq)
print(seq7)
print(repr({}))