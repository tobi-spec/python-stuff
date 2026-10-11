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

# user of class does not need to know how the email is created, it suffices that ist there
employee1 = Employee('John', 'Smith', 100)
print(employee1.email)