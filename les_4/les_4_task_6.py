# a
from itertools import count, cycle

for el in count(1):
    if el > 20:
        break
    else:
        print(el)

print('-' * 50)

# б
a = 0

for el in cycle('Vera K '):
    if a > 10:
        break
    print(el)
    a += 1
