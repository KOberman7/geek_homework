a = int(input('Choose a month: '))

#1-st variant (list)

winter = [1, 2, 12]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

if a == 1 or a == 2 or a== 12:
	print('Winter')
elif a == 3 or a == 4 or a == 5:
	print('Spring')
elif a == 6 or a == 7 or a == 8:
	print('Summer')
elif a== 9 or a == 10 or a == 11:
	print('Autumn')
else:
	print('Error')

#2-nd variant (dict)
seasons = {'Winter': (1, 2, 12),
           'Spring': (3, 4, 5),
           'Summer': (6, 7, 8),
           'Autumn': (9, 10, 11)}
 
month = int(input('Choose a month: '))
for key in seasons.keys():
    if month in seasons[key]:
        print(key)