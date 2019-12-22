f = open('second_file.txt')
line = 0
for i in f:
    line += 1
 
    word = 0
    for j in i:
        if j != ' ':
            word += 1
 
    print(f'Words: {word}')
 
print(f'Lines: {line}')
f.close()