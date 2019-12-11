a = int(input('Input first number: '))
b = int(input('Input second number: '))

try:
    c = a / b
except ZeroDivisionError:
    c = 0
    print("Can't be divided by zero.")

print(f'{a} / {b} = {int(c)}')
