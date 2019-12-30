class Office_equipment:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def __str__(self):
        return f'Name - {self.name}, model - {self.model}'


class Printer(Office_equipment):
    def __init__(self, name, model, amount):
        super().__init__(name, model)


class Scanner(Office_equipment):
    def __init__(self, name, model, amount):
        super().__init__(name, model)
        self.amount = amount


class Computer(Office_equipment):
    def __init__(self, name, model, amount):
        super().__init__(name, model)
        self.amount = amount


p = Printer('printer', 'RX-100', 10)
s = Scanner('scanner', 'Canon-SS2', 5)
c = Computer('computer', 'HP-ZCE378', 20)
print(f'{p},\n {s},\n {c}')

while True:
    print('1 - for break')
    order = input('What equipment do you need? (p - printer, s - scanner, c - computer) ')
    equipment = {}
    if order == 'p':
        printer = int(input('How many? '))
        equipment['printer'] = printer
        print(equipment)
    elif order == 's':
        scanner = int(input('How many? '))
        equipment['scanner'] = scanner
        print(equipment)
    elif order == 'c':
        computer = int(input('How many? '))
        equipment['computer'] = computer
        print(equipment)
    else:
        print(equipment)
        break
