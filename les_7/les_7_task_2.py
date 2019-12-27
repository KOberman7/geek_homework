from abc import abstractmethod


class Clothes:

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def material(self):
        pass


class Coat(Clothes):

    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def material(self):
        c = self.size / 6.5 + 0.5
        return f'Amount of fabric for coat - {int(c)}'


class Suit(Clothes):
    def __init__(self, name, hight):
        super().__init__(name)
        self.hight = hight

    @property
    def material(self):
        s = 2 * self.hight + 0.3
        return f'Amount of fabric for suit - {int(s)}'


new_coat = Coat('New collection', 50)
new_suit = Suit('Man', 165)
print(new_coat)
print(new_suit)
print(new_coat.material)
print(new_coat.material)
