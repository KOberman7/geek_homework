class Complex_number:
    def addition(self, a, b):
        print(f'{a + b}')

    def multiplication(self, a, b):
        print(f'{a * b}')


c_n = Complex_number()
print(c_n.addition(-5 + 3j, 4 + 2j))
print(c_n.multiplication(-5 + 3j, 4 + 2j))