import re
data = []
f = open("input.txt", "x+")
s = f.write('1 2 3 4 5')
values = f.read().split("\n")
data = []
 
for key in values:
    value = re.findall(r"[-+]?\d*\.\d+|\d+", key)
 
    if value != []:
        data.append(value)

sum = sum(data)
print(sum)

with open('output.txt', 'w') as file:
    file.write(str(sum))
f.close()