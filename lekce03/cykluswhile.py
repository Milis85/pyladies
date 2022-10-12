from os import lseek
from random import randrange
counter = 0
while True:
    if 13 == randrange(20):
        counter += 1
        print('tak to vyslo')
        print('trvalo to jenom ', + str(counter) + 'x')
        #print('trvalo to jenom ', counter, 'x')
        break
    print('smula')

