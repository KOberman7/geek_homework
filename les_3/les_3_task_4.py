# Первый способ

def my_func(x, y):
    c = x ** abs(y)
    return c


print(my_func(2, -3))


# Второй способ

def my_func(x, y):
    res = 1
    for i in range(abs(y)):
        res *= x
    if abs(y) >= 0:
        return res
    else:
        return 1 / res


print(my_func(2, -3))
