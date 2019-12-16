from functools import reduce

lst = [i for i in range(100, 1001) if i % 2 == 0]
print(lst)


def mult_el(prev_el, el):
    return prev_el * el


print(reduce(mult_el, lst))
