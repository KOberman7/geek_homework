def my_func(a, b, c):
    if a > b and c > b:
        return a + c
    elif b > a and c > a:
        return b + c
    else:
        return a + b


print(my_func(1, 2, 3))
print(my_func(2, 3, 1))
print(my_func(3, 1, 2))
