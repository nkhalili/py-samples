s = '''this is a     long 
string'''
# default split behavior
print(s.split())

# split on specific character
print(s.split('i'))

l = s.split()
# join with specific character
s2 = ':'.join(l)
s3 = '-'.join(l)
print(s2)
print(s3)