class Employee:
    def __init__(self, first: str, last: str) -> None:
        self.first: str = first
        self.last: str = last
        self.email: str = first + '.' + last + '@company.com'

    def fullname(self) -> str:
        return '{} {}'.format(self.first, self.last)

emp1 = Employee('John', 'Smith')

emp1.first ="Jim"

print(emp1.first)
print(emp1.fullname())
print(emp1.email)


