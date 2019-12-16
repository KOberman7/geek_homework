a = [int(i) for i in input('Input numbers with space: ').split()]
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        print(a[i])
