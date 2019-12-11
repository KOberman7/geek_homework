list_ = list(input('Input 4 numbers: '))

print(list_)

list_[0], list_[1] = list_[1], list_[0]

list_[2], list_[3] = list_[3], list_[2]

print(list_)