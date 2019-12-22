d = {}
with open("third_file.txt", "r") as file:
    for line in file:
        key, value = line.split()
        d[key] = value

        if int(value) < 20000:
            print(f'Employees whose salary is less than 20,000: {key}, {value}')
