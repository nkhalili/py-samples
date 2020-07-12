
def isprime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


n = 6
if isprime(n):
    print(f'{n} is prime')
else:
    print(f'{n} is not prime')
