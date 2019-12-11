string = input('Input a phrase: ').split()

print(string)

for word in string:
    if len(word) > 10:
        print(word[:10])
    else:
        print(word)