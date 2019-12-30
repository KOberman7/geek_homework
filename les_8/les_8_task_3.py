class StrError(Exception):
    def __init__(self, txt):
        self.txt = txt


while True:
    try:
        num = int(input('Input a number: '))
        b = []
        b.append(num)
        if type(num) == 'str':
            raise StrError('Don`t input string')
    except ValueError:
        print(StrError)
        if num == 'stop':
            break
            print(b)
