class Worker:
    name = 'Alex'
    surname = 'Emelov'
    position = 'Secretary'
    _income = {"wage": 40000, "bonus": 15000}
    get_full_name = name + ' ' + surname
    get_total_income = _income

class Position(Worker):

    def __init__(self):

        self.get_full_name = self.name + ' ' + self.surname
        self.get_total_income = self._income


w = Worker()
print(w.get_full_name)
print(w.get_total_income)
