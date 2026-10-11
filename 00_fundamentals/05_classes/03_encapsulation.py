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

    def get_half_payment(self) -> float:
        return self.__calculate_payment(0.5)

    # private
    def __calculate_payment(self, amount) -> float:
        return self.pay*amount

    # protected
    def _internal_method(self) -> str:
        return "This is protected!"

employee1 = Employee('John', 'Smith', 100)
print(employee1.get_half_payment())
print(employee1._internal_method())