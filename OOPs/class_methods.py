class Employee:
    '''
        Regular methods in class automatically take instance as their first argument.
        Whereas , class methods takes class as their first argument
        These class methods are used to create alternative constructors mostly.
        '''

    raiseAmount = 1.04
    no_of_emp = 0

    def __init__(self, first, last, pay):
        self.fname = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay
        Employee.no_of_emp += 1

    def fullname(self):
        return '{} {}'.format(self.fname, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raiseAmount)

    # to make regular method to class method add decorator to it
    @classmethod
    def set_raiseAmount(cls, amount):
        '''
        Silimar to regular methods , we use cls by the common convention (we can't use class as it is a keyword)
        '''
        cls.raiseAmount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        # this will instantiate new object of this class
        return cls(first, last, pay)


print(f"raiseAmount={Employee.raiseAmount}")
emp1 = Employee('Mothish', "MC", 50000)
emp2 = Employee("Hsihtom", "CM", 60000)
Employee.set_raiseAmount(1.05)  # equivalent to Employee.raiseAmount=1.05
# We can class methods by instances as well (ex: emp1.set_raiseAmount(1.05)),but it is not preferable
print("-----------------------")
print(Employee.raiseAmount)
print(emp1.raiseAmount)
print(emp2.raiseAmount, end='\n-----------------------\n')

emp_str_1 = "MC-Mothish-50000"
emp_str_2 = "CM-Hsihtom-60000"

new_emp_1 = Employee.from_string(emp_str_1)  # Alternative constructor
new_emp_2 = Employee.from_string(emp_str_2)

print(new_emp_1.email)
print(new_emp_2.pay)
