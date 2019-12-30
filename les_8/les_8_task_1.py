class Date:
    @classmethod
    def date(cls, day, month, year):
        print(f'Day - {int(day)}, month - {int(month)}, year - {int(year)}')

    @staticmethod
    def date_2(day, month, year):
        if day < 1 or day > 31:
            print('Invalid number of day')
        elif month < 1 or month > 12:
            print('Invalid number of month')
        elif year < 1900 or year > 1999:
            print('Invalid number of year')
        else:
            print(f'Day - {int(day)}, month - {int(month)}, year - {int(year)}')

Date.date(22, 12, 1985)
print(Date.date_2(32, 12, 1999))
print(Date.date_2(20, 15, 1999))
print(Date.date_2(20, 12, 2000))
print(Date.date_2(12, 1, 1999))