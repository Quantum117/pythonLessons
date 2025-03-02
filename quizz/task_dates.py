import datetime

from pandas.core.computation.ops import isnumeric


class Dates :
    @staticmethod
    def check_numeric(string):
        for c in string.strip():
            if not isnumeric(c):
                raise ValueError

    def __init__(self, day, month, year):
        try:
            if int(day)<1 or int(day)>31:
                raise ValueError

            else:
                self.day = int(day)
            if int(month)<1 or int(month)>12:
                raise ValueError
            else:
                self.month = month
            self.year = year
        except ValueError:
            print("Enter appropriate values to days and months ")

    def print_numeric(self):
        print(f"{self.day}/{self.month}/{self.year}")

    def print_2(self):
        print(f"{self.day}/{self.month}/{self.year}")

    def print_3(self):
        print(f"{self.day}/{self.month}/{self.year}")

date = Dates(11,12,2002)

date.print_numeric()