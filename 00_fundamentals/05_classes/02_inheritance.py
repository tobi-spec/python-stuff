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


class Developer(Employee):
    def __init__(self, first: str, last: str, pay: int, programming_language: str) -> None:
        super().__init__(first, last, pay)
        self.programming_language = programming_language


dev = Developer('John', 'Smith', 50000, 'Python')
print(dev.fullname())
print(dev.programming_language)