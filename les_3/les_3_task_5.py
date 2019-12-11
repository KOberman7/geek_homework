s = 0

try:
    while True:
        for n in map(int, input('Input numbers with space: ').split()):
            s += n
        print(s)
except ValueError:
    print('Invalid character')
    print(s)
