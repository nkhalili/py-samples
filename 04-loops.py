# fibonacci series

a, b = 0, 1
while b < 1000:
    print(b, end=' ', flush=True)
    a, b = b, a + b

print()


# for sample
words = ['one', 'two', 'three', 'four', 'five']

for i in words:
    print(i)
