import sys
import os
import random
import datetime

def main():
    v = sys.version_info
    print('Python version: {}.{}.{} {}'.format(*v))
    #print(f'Python version: {v.major}.{v.minor}.{v.micro}')

    p = sys.platform
    print(f'Platform: {p}')

    os_name = os.name
    print(f'OS: {os_name}')

    os_path = os.getenv('PATH')
    print(f'Path: {os_path}')

    cwd = os.getcwd()
    print(f'Current working directory: {cwd}')

    # generates random number with the specified length
    osr = os.urandom(2).hex() 
    print(f'{osr}')
    
    ri = random.randint(1, 1000)
    print(f'Random number: {ri}')

    r = list(range(25))
    print(r)
    random.shuffle(r)
    print(r)

    now = datetime.datetime.now()
    print(f'Now: {now}')
    print(f'Year: {now.year}, Month: {now.month}, Day: {now.day}, h: {now.hour}, m: {now.minute}, s: {now.second}')

if __name__ == "__main__":
    main()