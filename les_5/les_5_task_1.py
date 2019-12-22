f = open('my_first_file.txt', 'x+')

while True:

    s = input('Input a phrase: ')

    if s == '': break
    f.write(s + '\n')

f.close()
