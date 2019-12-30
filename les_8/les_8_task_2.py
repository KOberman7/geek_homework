class ZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt

try:
    data_1 = int(input('Input first number: '))
    data_2 = int(input('Input second number: '))
    if data_2 == 0:
        raise ZeroError('DON`T DIVIDE ON 0!!!')
except ZeroError as err:
    print(err)
else:
    c = data_1 / data_2
    print('OK')
    print(c)
