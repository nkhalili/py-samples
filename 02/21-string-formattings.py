x = 42
y = 73
print('the number is {} {}'.format(x, y))
# for python +3.6 all the formatting options work for this too
print(f'the number is {x} {y}')

print('the number is {a} {b}'.format(a=x, b=y))
print('the number is {b} {a}'.format(a=x, b=y))
print('the number is {0} {1}'.format(x, y))
print('the number is {1} {0}'.format(x, y))
print('the number is {1} {0} {1}'.format(x, y))

# add spaces after or before, value itself counts
print('the number is "{0:<5}" "{1:>5}"'.format(x, y))
# add zero and plus sign
print('the number is "{0:03}" "{1:+05}"'.format(x, y))

# comma formatting thousand separation
print('the number is {:,}'.format(1000000))
# for europe
print('the number is {:,}'.format(1000000).replace(',', '.'))

# decimal point e.g 3 decimal places
print('the number is {:.3f}'.format(1000000))

# hexadecimal formatting
print('the number is {:x}'.format(42))
# octal
print('the number is {:o}'.format(42))
# binary
print('the number is {:b}'.format(42))
