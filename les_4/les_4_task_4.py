lst = [3, 1, 2, 4, 5, 6, 2, 5, 2, 8]

used = set()
unique = [x for x in lst if x not in used and (used.add(x) or True)]
print(unique)
