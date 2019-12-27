class Cell:
    def __init__(self, cell_1, cell_2):
        self.cell_1 = cell_1
        self.cell_2 = cell_2

    def make_oder(self, rows):
        self.rows = rows

    def __add__(self, other):
        return Cell(self.cell_1 + other.cell_1, self.cell_2 + other.cell_2)

    def __sub__(self):
		pass
            
    
    def __mul__(self):
        pass
    
    def __truediv__(self):
        pass

a = Cell(10,22)
b = Cell(22,10)
z = a + b
print(z)

print(Cell.make_oder(7))