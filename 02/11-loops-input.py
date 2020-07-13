secret = "secret"
pw = ''

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