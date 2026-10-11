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

employee1 = Employee('John', 'Smith', 100)
print(employee1.fullname())

print(Employee.fullname(employee1))

employee2 = Employee('Jean', 'Doe', 200)
print(employee2.email)

print(employee2.__dict__)
employee2.apply_raise()
print(employee2.__dict__)

print(Employee.__dict__)


