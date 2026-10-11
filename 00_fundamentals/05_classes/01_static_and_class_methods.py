from datetime import date


class Employee:
    raise_amount = 1.04

    def __init__(self, first: str, last: str, pay: int) -> None:
        self.first: str = first
        self.last: str = last
        self.pay: int = pay
        self.email: str = first + '.' + last + '@company.com'

    def fullname(self) -> str:
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = self.pay * self.raise_amount

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # alternativ constructor
    @classmethod
    def from_string(cls, string):
        first, last, pay = string.split("-")
        return cls(first, last, int(pay))

    @staticmethod
    def is_workday(day: date) -> bool:
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

employee1 = Employee('John', 'Smith', 100)
employee2 = Employee('Jean', 'Doe', 200)

Employee.set_raise_amount(1.10)


emp_str1 = "John-Doe-300"
new_employee2 = Employee.from_string(emp_str1)
print(new_employee2.fullname())

my_date: date = date(2020, 1, 1)
print(Employee.is_workday(my_date))
