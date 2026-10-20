class Employee:
    def __init__(self, first: str, last: str) -> None:
        self.first: str = first
        self.last: str = last

    @property
    def email(self) -> str:
        return self.first + '.' + self.last + '@company.com'

    @property
    def fullname(self) -> str:
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name: str) -> None:
        self.first, self.last = name.split()

    @fullname.deleter
    def fullname(self) -> None:
        del self.first, self.last


emp1 = Employee('John', 'Smith')

emp1.first ="Jim"
print(emp1.first)
print(emp1.fullname)
print(emp1.email)

emp1.fullname = "Jakob Jay"
print(emp1.first)
print(emp1.fullname)
print(emp1.email)

del emp1.fullname
try:
    print(emp1.first)
    print(emp1.fullname)
except AttributeError as e:
    print(e)