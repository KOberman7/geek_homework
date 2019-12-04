earnings = int(input('Введите текущую прибыль фирмы: '))
cost = int(input('Введите кол-во издержек: '))

profit = earnings / cost

if earnings > cost:
	print('Фирма работает на прибыль')
	print(f'Прибыль составляет: {profit}')
	print(f'Рентабельность выручки: {profit / earnings} ')
else:
	print('Фирма работает в убыток')

emp = int(input('Введите кол-во сотрудников: '))

profit_e = profit / emp

print(profit_e)