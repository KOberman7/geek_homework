import re

with open('1.txt') as file:
    content = file.readlines()

d = {}
for line in content:
    key, value = line.split('-')
    d[key] = value

d['One '] = 'Один'
d['Two '] = 'Два'
d['Three '] = 'Три'
d['Four '] = 'Четыре'

with open('d_dict.txt', 'x+') as file:
    file.write(str(d))
file.close()
